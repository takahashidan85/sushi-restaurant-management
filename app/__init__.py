from flask import Flask
from .config import Config
from .extensions import db, migrate
from .presentation import register_blueprints

def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_object(Config)
    if test_config:
        app.config.update(test_config)

    # init extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # register routes
    register_blueprints(app)

    @app.get("/")
    def index():
        return {"status": "ok", "app": "sushi-restaurant-management"}

    return app
