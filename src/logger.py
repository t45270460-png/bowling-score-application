from logging import getLogger, StreamHandler, Formatter, DEBUG


def setup_logger():
    logger = getLogger("bowling_app")
    logger.setLevel(DEBUG)

    handler = StreamHandler()
    handler.setLevel(DEBUG)

    formatter = Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    return logger


logger = setup_logger()
