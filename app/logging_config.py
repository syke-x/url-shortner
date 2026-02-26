import logging
from logging.config import dictConfig


def setup_logging():
    dictConfig({
        "version": 1,
        "disable_existing_loggers": False,

        "formatters": {
            "standard": {
                "format": "%(asctime)s [%(levelname)s] [%(name)s] %(message)s"
            },
            "json": {
                "format": '{"time":"%(asctime)s","level":"%(levelname)s","module":"%(name)s","message":"%(message)s"}'
            }
        },

        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "standard",
            },
            "file": {
                "class": "logging.handlers.RotatingFileHandler",
                "filename": "logs/app.log",
                "maxBytes": 10_000_000,
                "backupCount": 5,
                "formatter": "standard",
            }
        },

        "root": {
            "level": "INFO",
            "handlers": ["console", "file"]
        }
    })