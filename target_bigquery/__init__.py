#!/usr/bin/env python3

import argparse
import io
import json
import sys
import traceback

import singer

from target_bigquery.encoders import DecimalEncoder
from target_bigquery.process import process
from target_bigquery.schema import build_schema, filter
from target_bigquery.utils import emit_state, ensure_dataset

logger = singer.get_logger()


def main():
    parser = argparse.ArgumentParser()  # argparse.ArgumentParser(parents=[tools.argparser])
    parser.add_argument("-c", "--config", help="Config file", required=True)
    parser.add_argument("-t", "--tables", help="Table configs file", required=False)
    parser.add_argument("-s", "--state", help="Initial state file", required=False)
    parser.add_argument("-ph", "--processhandler",
                        help="Defines the loading process. Partial loads by default.",
                        required=False,
                        choices=["load-job", "partial-load-job", "bookmarks-partial-load-job", "streaming-inserts"],
                        default="partial-load-job"
                        )
    flags = parser.parse_args()

    with open(flags.config) as f:
        config = json.load(f)

    tables = {}
    if flags.tables is not None:
        with open(flags.tables) as f:
            tables = json.load(f)

    state = {}
    if flags.state is not None:
        with open(flags.state) as f:
            state = json.load(f)

    truncate = False
    if config.get("replication_method", "append").lower() == "truncate":
        truncate = True

    table_prefix = config.get("table_prefix", "")
    table_suffix = config.get("table_suffix", "")
    location = config.get("location", "US")
    validate_records = config.get("validate_records", True)
    add_metadata_columns = config.get("add_metadata_columns", True)
    project_id, dataset_id = config["project_id"], config["dataset_id"]

    table_configs = tables.get("streams", {})
    max_cache = 1024 * 1024 * config.get("max_cache", 50)

    tap_stream = io.TextIOWrapper(sys.stdin.buffer, encoding="utf-8")

    client, dataset = ensure_dataset(project_id, dataset_id, location)

    try:
        from target_bigquery.processhandler import LoadJobProcessHandler, PartialLoadJobProcessHandler, \
            BookmarksStatePartialLoadJobProcessHandler, StreamingInsertsProcessHandler

        ph = None
        if flags.processhandler == "load-job":
            ph = LoadJobProcessHandler
        elif flags.processhandler == "partial-load-job":
            ph = PartialLoadJobProcessHandler
        elif flags.processhandler == "bookmarks-partial-load-job":
            ph = BookmarksStatePartialLoadJobProcessHandler
        elif flags.processhandler == "streaming-inserts":
            ph = StreamingInsertsProcessHandler
        else:
            raise Exception("Unknown process handler.")

        state_iterator = process(
            ph,
            tap_stream,
            initial_state=state,
            project_id=project_id,
            dataset=dataset,
            location=location,
            truncate=truncate,
            validate_records=validate_records,
            table_prefix=table_prefix,
            table_suffix=table_suffix,
            add_metadata_columns=add_metadata_columns,
            table_configs=table_configs,
            max_cache=max_cache
        )

        for state in state_iterator:
            emit_state(state)

    except Exception as e:
        # load errors surface here
        logger.critical(e)
        exc_type, exc_value, exc_traceback = sys.exc_info()
        logger.critical(repr(traceback.format_exception(exc_type, exc_value, exc_traceback)))
        return 2  # sys.exit(2)

    return 0  # sys.exit(0)


if __name__ == "__main__":
    ret = main()
    sys.exit(ret)
