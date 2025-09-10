import logging
import os
from logging.handlers import RotatingFileHandler
from flask.logging import default_handler
from flask import request

def configure_logging(app):
    """Configure logging for the application."""

    log_level = logging.DEBUG if app.debug else logging.INFO
    app.logger.setLevel(log_level)

    """File Handler (Actions)"""
    action_file_handler = RotatingFileHandler('logs/actions.log', maxBytes=10240, backupCount=10)
    action_file_handler.setLevel(log_level)

    """File Handler (Error)"""
    error_file_handler = RotatingFileHandler('logs/errors.log', maxBytes=10240, backupCount=10)
    error_file_handler.setLevel(logging.ERROR)

    if not os.path.exists('logs'):
        os.makedirs('logs')

    formatter = logging.Formatter(
        "[%(asctime)s] - %(name)s - %(levelname)s - %(message)s"
    )
    action_file_handler.setFormatter(formatter)
    error_file_handler.setFormatter(formatter)

    if default_handler not in app.logger.handlers:
        app.logger.addHandler(default_handler)

    app.logger.addHandler(action_file_handler)
    app.logger.addHandler(error_file_handler)

    app.logger.info("Logging is set up.")

def setup_request_logging(app):
    """Request and response log for APIs."""
    @app.before_request
    def log_request_info():
        app.logger.info(f"{request.method} {request.path}")

    @app.after_request
    def log_response_info(response):
        app.logger.info(f"{request.method} {request.path} - {response.status}")
        return response