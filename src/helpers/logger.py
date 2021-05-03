"""This helper module logs messages of different severity levels"""
import logging
import sys

logger = logging.getLogger("harvest_data_validator")
app_log_handler = logging.StreamHandler(sys.stdout)
app_log_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")
app_log_handler.setFormatter(app_log_formatter)
logger.addHandler(app_log_handler)


def info(message: str):
    """Logs general information

    Parameters
    ----------
    message
        Message input
    """
    logger.setLevel(logging.INFO)
    logger.info(message)


def error(message: str):
    """Logs error information

    Parameters
    ----------
    message
        Message input
    """
    logger.setLevel(logging.ERROR)
    logger.error(message)


def warning(message: str):
    """Logs error information

    Parameters
    ----------
    message
        Message input
    """
    logger.setLevel(logging.WARNING)
    logger.warning(message)
