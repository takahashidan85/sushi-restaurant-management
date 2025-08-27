from flask import Flask
from flasgger import Swagger
from .presentation import register_blueprints
from .extensions import db, migrate
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    Swagger(app)
    register_blueprints(app)
    
    return app
