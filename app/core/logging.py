import logging
from logging.handlers import RotatingFileHandler
import os

def configure_logging(app):
    """Configure logging for the application."""

    log_level = logging.DEBUG if app.debug else logging.INFO

    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)

    if not os.path.exists('logs'):
        os.makedirs('logs')
    file_handler = RotatingFileHandler('logs/app.log', maxBytes=10240, backupCount=10)
    file_handler.setLevel(log_level)

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    app.logger.setLevel(log_level)
    app.logger.addHandler(console_handler)
    app.logger.addHandler(file_handler)

    app.logger.info("Logging is set up.")