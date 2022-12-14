import logging


def getLogger(name):
    formatter = logging.Formatter(fmt=(
        "%(name)s:%(lineno)s %(funcName)s [%(levelname)s]: %(message)s"
    ))

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)
    return logger
