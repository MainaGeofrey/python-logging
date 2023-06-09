import logging.config


class LevelOnlyFilter:
    def __init__(self, level):
        self.level = level

    def filter(self, record):
        return record.levelno == self.level


LOGGING_CONFIG = {
    "version": 1,
    "loggers": {
        "": {  # root logger
            "level": "DEBUG",
            "propagate": False,
            "handlers": ["stream_handler", "file_handler"],
        },
        "custom_logger": {
            "level": "DEBUG",
            "propagate": False,
            "handlers": ["stream_handler"],
        },
    },
    "handlers": {
        "stream_handler": {
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
            "level": "DEBUG",
            "filters": ["only_warning"],
            "formatter": "default_formatter",
        },
        "file_handler": {
            "class": "logging.FileHandler",
            "filename": "output.log",
            "mode": "a",
            "level": "DEBUG",
            "formatter": "default_formatter",
        },
    },
    "filters": {
        "only_warning": {
            "()": LevelOnlyFilter,
            "level": logging.WARN,
        },
    },
    "formatters": {
        "default_formatter": {
            "format": "%(asctime)s-%(levelname)s-%(name)s::%(module)s|%(lineno)s:: %(message)s",
        },
    },
}

"""logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger(__name__)

try:
    raise Exception("Throw exception")
except Exception as e:
    logger.error("Exception occurred") """
    
#import logging this way
import logging.config
logging.config.fileConfig("logging.conf")
logger = logging.getLogger(__name__)