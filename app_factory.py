from flask import Flask
from app.core.config import Config
from app.core.extensions import db, migrate
from app.core.error_handler import register_error_handlers
from app.core.logging import configure_logging
from app.modules import (
    customer_bp,
    order_bp,
    sushi_item_bp,
    order_detail_bp
)

def create_app(config_class=Config):
    """Application factory function."""
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Init extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Logging
    configure_logging(app)

    # Error handlers
    register_error_handlers(app)

    # Register blueprints
    app.register_blueprint(customer_bp)
    app.register_blueprint(order_bp)
    app.register_blueprint(sushi_item_bp)
    app.register_blueprint(order_detail_bp)

    return app
