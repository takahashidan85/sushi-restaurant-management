from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint
from flask_cors import CORS
from app.core.config import Config
from app.core.extensions import db, migrate
from app.core.error_handler import register_error_handlers
from app.core.logging import configure_logging, setup_request_logging
from app.modules import (
    customer_bp,
    order_bp,
    sushi_item_bp,
    order_detail_bp
)

SWAGGER_URL = "/swagger"
API_URL = "http://127.0.0.1:5000/static/swagger.json"

swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={"app_name": "Sushi Restaurant Management API"},
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
    setup_request_logging(app)

    # Error handlers
    register_error_handlers(app)

    # Enable CORS
    CORS(app, resources={r"/*": {"origins": "*"}})

    # Register blueprints
    app.register_blueprint(customer_bp)
    app.register_blueprint(order_bp)
    app.register_blueprint(sushi_item_bp)
    app.register_blueprint(order_detail_bp)

    app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

    """Health check to test if API works."""
    @app.route("/ping")
    def ping():
        return {"message": "pong"}, 200

    return app


