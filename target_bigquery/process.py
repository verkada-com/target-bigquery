import json

import singer

from target_bigquery.processhandler import BaseProcessHandler

logger = singer.get_logger()


def process(
        ProcessHandler,
        tap_stream,
        **kwargs
):
    handler = ProcessHandler(logger, **kwargs)
    assert isinstance(handler, BaseProcessHandler)

    if handler.emit_initial_state():
        s = kwargs.get("initial_state", {})
        assert isinstance(s, dict)
        logger.info(f"Pushing state: {s}")
        yield s  # yield init state, so even if there is an exception right after we get proper state emitted

    for line in tap_stream:
        try:
            msg = singer.parse_message(line)
        except json.decoder.JSONDecodeError:
            logger.error("Unable to parse:\n{}".format(line))
            raise

        if isinstance(msg, singer.RecordMessage):
            for s in handler.handle_record_message(msg):
                logger.info(f"Pushing state: {s}")
                yield s

        elif isinstance(msg, singer.StateMessage):
            logger.info("Updating state with {}".format(msg.value))
            for s in handler.handle_state_message(msg):
                logger.info(f"Pushing state: {s}")
                yield s

        elif isinstance(msg, singer.SchemaMessage):
            logger.info("{} schema: {}".format(msg.stream, msg.schema))
            for s in handler.handle_schema_message(msg):
                logger.info(f"Pushing state: {s}")
                yield s

        elif isinstance(msg, singer.ActivateVersionMessage):
            # This is experimental and won't be used yet
            pass

        else:
            raise Exception("Unrecognized message {}".format(msg))

    for s in handler.on_stream_end():
        logger.info(f"Pushing state: {s}")
        yield s
