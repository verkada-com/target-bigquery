import json
import uuid
from datetime import datetime
from tempfile import TemporaryFile

import singer
from google.api_core import exceptions as google_exceptions
from google.cloud import bigquery
from google.cloud.bigquery import LoadJobConfig, CopyJobConfig
from google.cloud.bigquery import WriteDisposition
from google.cloud.bigquery.job import SourceFormat
from jsonschema import validate

from target_bigquery.encoders import DecimalEncoder
from target_bigquery.schema import build_schema, filter as filter_by_schema
from target_bigquery.state import State


class BaseProcessHandler(object):

    def __init__(self, logger, **kwargs):
        self.logger = logger

        self.project_id = kwargs["project_id"]
        self.dataset = kwargs["dataset"]

        self.table_prefix = kwargs.get("table_prefix") or ""
        self.table_suffix = kwargs.get("table_suffix") or ""

        self.tables = {}
        self.schemas = {}
        self.key_properties = {}

    def emit_initial_state(self):
        return True

    def handle_record_message(self, msg):
        raise NotImplementedError()

    def handle_state_message(self, msg):
        raise NotImplementedError()

    def handle_schema_message(self, msg):
        assert isinstance(msg, singer.SchemaMessage)

        # only first schema sent per stream is saved
        if msg.stream in self.tables:
            return iter([])

        self.tables[msg.stream] = "{}{}{}".format(
            self.table_prefix, msg.stream, self.table_suffix
        )
        self.schemas[msg.stream] = msg.schema
        self.key_properties[msg.stream] = msg.key_properties

        yield from ()

    def on_stream_end(self):
        yield from ()


class LoadJobProcessHandler(BaseProcessHandler):

    def __init__(self, logger, **kwargs):
        super(LoadJobProcessHandler, self).__init__(logger, **kwargs)

        self.truncate = kwargs.get("truncate", False)
        self.partially_loaded_streams = set()
        self.add_metadata_columns = kwargs.get("add_metadata_columns", True)
        self.validate_records = kwargs.get("validate_records", True)
        self.table_configs = kwargs.get("table_configs", {}) or {}

        self.INIT_STATE = kwargs.get("init_state") or {}
        self.STATE = State(**self.INIT_STATE)

        self.rows = {}

        self.client = bigquery.Client(
            project=self.project_id,
            location=kwargs.get("location", "US")
        )

    def handle_schema_message(self, msg):
        for s in super(LoadJobProcessHandler, self).handle_schema_message(msg):
            yield s

        if msg.stream not in self.rows:
            self.rows[msg.stream] = TemporaryFile(mode="w+b")

        yield from ()

    def handle_record_message(self, msg):
        assert isinstance(msg, singer.RecordMessage)

        stream = msg.stream

        if stream not in self.schemas:
            raise Exception(f"A record for stream {msg.stream} was encountered before a corresponding schema")

        schema = self.schemas[stream]

        if self.validate_records:
            validate(msg.record, schema)

        if self.add_metadata_columns:
            msg.record["_time_extracted"] = msg.time_extracted.isoformat() \
                if msg.time_extracted else datetime.utcnow().isoformat()
            msg.record["_time_loaded"] = datetime.utcnow().isoformat()

        new_rec = filter_by_schema(schema, msg.record)

        data = bytes(json.dumps(new_rec, cls=DecimalEncoder) + "\n", "UTF-8")
        self.rows[stream].write(data)

        yield from ()

    def handle_state_message(self, msg):
        assert isinstance(msg, singer.StateMessage)

        self.STATE.merge(msg.value)

        yield from ()

    def on_stream_end(self):
        self._do_temp_table_based_load(self.rows)
        yield self.STATE

    def _do_temp_table_based_load(self, rows):
        assert isinstance(rows, dict)

        loaded_tmp_tables = []
        try:
            for stream in rows.keys():
                tmp_table_name = "t_{}_{}".format(self.tables[stream], str(uuid.uuid4()).replace("-", ""))

                job = self._load_to_bq(
                    client=self.client,
                    dataset=self.dataset,
                    table_name=tmp_table_name,
                    table_schema=self.schemas[stream],
                    table_config=self.table_configs.get(stream, {}),
                    key_props=self.key_properties[stream],
                    metadata_columns=self.add_metadata_columns,
                    truncate=self.truncate if stream not in self.partially_loaded_streams else False,
                    rows=self.rows[stream]
                )

                loaded_tmp_tables.append((stream, tmp_table_name))

            # copy tables to production tables
            copy_config = CopyJobConfig()
            copy_config.write_disposition = WriteDisposition.WRITE_APPEND

            for stream, tmp_table_name in loaded_tmp_tables:
                self.logger.info(f"Copy {tmp_table_name} to {self.tables[stream]}")

                self.client.copy_table(
                    sources=self.dataset.table(tmp_table_name),
                    destination=self.dataset.table(self.tables[stream]),
                    job_config=copy_config
                ).result()

                self.partially_loaded_streams.add(stream)
                self.rows[stream].close()  # erase the file
                self.rows[stream] = TemporaryFile(mode="w+b")

        except Exception as e:
            raise e

        finally:  # delete temp tables
            for stream, tmp_table_name in loaded_tmp_tables:
                self.client.delete_table(table=self.dataset.table(tmp_table_name), not_found_ok=True)

    def _load_to_bq(self,
                    client,
                    dataset,
                    table_name,
                    table_schema,
                    table_config,
                    key_props,
                    metadata_columns,
                    truncate,
                    rows):
        logger = self.logger
        partition_field = table_config.get("partition_field", None)
        cluster_fields = table_config.get("cluster_fields", None)
        force_fields = table_config.get("force_fields", {})

        schema = build_schema(table_schema, key_properties=key_props, add_metadata=metadata_columns, force_fields=force_fields)
        load_config = LoadJobConfig()
        load_config.schema = schema
        if partition_field:
            load_config.time_partitioning = bigquery.table.TimePartitioning(
                type_=bigquery.table.TimePartitioningType.DAY,
                field=partition_field
            )

        if cluster_fields:
            load_config.clustering_fields = cluster_fields

        load_config.source_format = SourceFormat.NEWLINE_DELIMITED_JSON

        if truncate:
            logger.info(f"Load {table_name} by FULL_TABLE (truncate)")
            load_config.write_disposition = WriteDisposition.WRITE_TRUNCATE
        else:
            logger.info(f"Appending to {table_name}")
            load_config.write_disposition = WriteDisposition.WRITE_APPEND

        logger.info("loading {} to BigQuery".format(table_name))

        load_job = None
        try:
            load_job = client.load_table_from_file(
                rows, dataset.table(table_name), job_config=load_config, rewind=True
            )
            logger.info("loading job {}".format(load_job.job_id))
            job = load_job.result()
            logger.info(job._properties)

            return job

        except google_exceptions.BadRequest as err:
            logger.error(
                "failed to load table {} from file: {}".format(table_name, str(err))
            )
            if load_job and load_job.errors:
                reason = err.errors[0]["reason"]
                messages = [f"{err['message']}" for err in load_job.errors]
                logger.error("reason: {reason}, errors:\n{e}".format(reason=reason, e="\n".join(messages)))
                err.message = f"reason: {reason}, errors: {';'.join(messages)}"

            raise err


class PartialLoadJobProcessHandler(LoadJobProcessHandler):

    def __init__(self, logger, **kwargs):
        super(PartialLoadJobProcessHandler, self).__init__(logger, **kwargs)

        self.max_cache = kwargs.get("max_cache", 1024 * 1024 * 50)

    def handle_state_message(self, msg):
        assert isinstance(msg, singer.StateMessage)
        for s in super(PartialLoadJobProcessHandler, self).handle_state_message(msg):
            yield s

        if sum([self.rows[s].tell() for s in self.rows.keys()]) > self.max_cache:
            rows = {s: self.rows[s] for s in self.rows.keys() if self.rows[s].tell() > 0}
            self._do_temp_table_based_load(rows)

            yield self.STATE

    def on_stream_end(self):
        rows = {s: self.rows[s] for s in self.rows.keys() if self.rows[s].tell() > 0}
        if len(rows) == 0:
            return iter([])

        self._do_temp_table_based_load(rows)
        yield self.STATE


class BookmarksStatePartialLoadJobProcessHandler(PartialLoadJobProcessHandler):

    def __init__(self, logger, **kwargs):
        super(BookmarksStatePartialLoadJobProcessHandler, self).__init__(logger, **kwargs)

        self.EMITTED_STATE = State(**self.INIT_STATE)

    def handle_state_message(self, msg):
        assert isinstance(msg, singer.StateMessage)
        for s in super(PartialLoadJobProcessHandler, self).handle_state_message(msg):
            yield s

        if sum([self.rows[s].tell() for s in self.rows.keys()]) > self.max_cache:
            rows = {s: self.rows[s] for s in self.rows.keys() if self.rows[s].tell() > 0}
            for stream in rows.keys():
                self._do_temp_table_based_load({stream: rows[stream]})

                self.EMITTED_STATE["bookmarks"][stream] = self.STATE["bookmarks"][stream]

                yield self.EMITTED_STATE

    def on_stream_end(self):
        rows = {s: self.rows[s] for s in self.rows.keys() if self.rows[s].tell() > 0}
        if len(rows) == 0:
            return iter([])

        for stream in rows.keys():
            self._do_temp_table_based_load({stream: rows[stream]})

            self.EMITTED_STATE["bookmarks"][stream] = self.STATE["bookmarks"][stream]

            yield self.EMITTED_STATE


class StreamingInsertsProcessHandler(BaseProcessHandler):

    def __init__(self, logger, **kwargs):
        super(StreamingInsertsProcessHandler, self).__init__(logger, **kwargs)

        # self.truncate = kwargs.get("truncate", False)
        # self.partially_loaded_streams = set()
        self.add_metadata_columns = kwargs.get("add_metadata_columns", True)
        self.validate_records = kwargs.get("validate_records", True)
        self.table_configs = kwargs.get("table_configs", {}) or {}
        #
        self.INIT_STATE = kwargs.get("init_state") or {}
        self.STATE = State(**self.INIT_STATE)
        #
        # self.rows = {}

        self.client = bigquery.Client(
            project=self.project_id,
            location=kwargs.get("location", "US")
        )

        self.table_refs = {}

    # def emit_initial_state(self):
    #     return False

    def handle_schema_message(self, msg):
        stream = msg.stream
        if stream not in self.schemas:
            self.table_refs[stream] = self._ensure_table(client=self.client,
                                                         dataset=self.dataset,
                                                         table_name="{}{}{}".format(self.table_prefix, msg.stream, self.table_suffix),
                                                         table_schema=msg.schema,
                                                         table_config=self.table_configs.get(stream, {}),
                                                         key_props=msg.key_properties,
                                                         metadata_columns=self.add_metadata_columns)

        for s in super(StreamingInsertsProcessHandler, self).handle_schema_message(msg):
            yield s

        yield from ()

    def handle_record_message(self, msg):
        assert isinstance(msg, singer.RecordMessage)

        stream = msg.stream

        if stream not in self.schemas:
            raise Exception(f"A record for stream {msg.stream} was encountered before a corresponding schema")

        schema = self.schemas[stream]

        if self.validate_records:
            validate(msg.record, schema)

        if self.add_metadata_columns:
            msg.record["_time_extracted"] = msg.time_extracted.isoformat() \
                if msg.time_extracted else datetime.utcnow().isoformat()
            msg.record["_time_loaded"] = datetime.utcnow().isoformat()

        new_rec = filter_by_schema(schema, msg.record)
        new_rec = json.loads(json.dumps(new_rec, cls=DecimalEncoder))

        self._stream_to_bq(client=self.client, table_ref=self.table_refs[stream], row=[new_rec])

        yield from ()

    def handle_state_message(self, msg):
        assert isinstance(msg, singer.StateMessage)

        self.STATE.merge(msg.value)

        yield self.STATE

    def on_stream_end(self):
        # self._stream_to_bq(self.rows)
        yield self.STATE

    def _ensure_table(self,
                    client,
                    dataset,
                    table_name,
                    table_schema,
                    table_config,
                    key_props,
                    metadata_columns):
        """
        Ensure the table exists with partitioning/clustering
        & returns a table reference to save for streaming
        """
        logger = self.logger
        partition_field = table_config.get("partition_field", None)
        cluster_fields = table_config.get("cluster_fields", None)
        force_fields = table_config.get("force_fields", {})

        schema = build_schema(table_schema, key_properties=key_props, add_metadata=metadata_columns, force_fields=force_fields)

        try:
            # dataset_ref = bigquery.DatasetReference(project, dataset)
            table_ref = dataset.table(table_name)
            table = bigquery.Table(table_ref, schema=schema)

            if partition_field:
                table.time_partitioning = bigquery.table.TimePartitioning(
                    type_=bigquery.table.TimePartitioningType.DAY,
                    field=partition_field
                )

            if cluster_fields:
                table.clustering_fields = cluster_fields

            table = client.create_table(table, exists_ok=True) # supposedly exists_ok ignores related errors
            logger.info(f"table created: {dataset}.{table_name}")
            return dataset.table(table.table_id)

        except Exception as e:
            logger.error(f"failed to ensure table exists: {dataset}.{table_name}")
            raise e


    def _stream_to_bq(self,
                    client,
                    table_ref,
                    row):
        logger = self.logger

        errors = None
        try:
            errors = client.insert_rows_json(table_ref, row)
            if errors != []:
                errs = '\n'.join(errors)
                logger.error(f"failed to insert rows for {table_ref.table_id}: {errs}\noffending record: {row}")
                raise Exception(errors)
        except Exception as err:
            logger.error(
                "failed to stream to table {}: {}".format(table_ref.table_id, str(err))
            )
            raise err

# class BookmarksStreamingInsertsProcessHandler(StreamingInsertsProcessHandler):
#
#     def __init__(self, logger, **kwargs):
#         super(BookmarksStreamingInsertsProcessHandler, self).__init__(logger, **kwargs)
#
#         self.EMITTED_STATE = State(**self.INIT_STATE)
#
#     def handle_state_message(self, msg):
#         assert isinstance(msg, singer.StateMessage)
#         for s in super(StreamingInsertsProcessHandler, self).handle_state_message(msg):
#             yield s
#
#         self.EMITTED_STATE["bookmarks"][stream] = self.STATE["bookmarks"][stream]
#
#         yield self.EMITTED_STATE
#
#     def on_stream_end(self):
#         rows = {s: self.rows[s] for s in self.rows.keys() if self.rows[s].tell() > 0}
#         if len(rows) == 0:
#             return iter([])
#
#         for stream in rows.keys():
#             self._do_temp_table_based_load({stream: rows[stream]})
#
#             self.EMITTED_STATE["bookmarks"][stream] = self.STATE["bookmarks"][stream]
#
#             yield self.EMITTED_STATE