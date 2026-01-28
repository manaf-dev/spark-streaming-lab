import logging


# set up logging to log file
def get_logger(name: str) -> logging.Logger:
    """Function to set up a logger with specified name, log file, and level."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # create file handler which logs even debug messages
    fh = logging.FileHandler("logs.log")
    fh.setLevel(logging.INFO)

    # create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.ERROR)

    # create formatter and add it to the handlers
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    # add the handlers to the logger
    logger.addHandler(fh)
    logger.addHandler(ch)

    return logger
