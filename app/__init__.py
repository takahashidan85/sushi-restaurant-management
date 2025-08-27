from flask import Flask
from flasgger import Swagger
from .presentation import register_blueprints

def create_app():
    app = Flask(__name__)
    Swagger(app)
    register_blueprints(app)
    return app
