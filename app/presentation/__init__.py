from flask import Flask
from flasgger import Swagger
from .customer_route import customer_bp
from .sushi_item_route import sushi_item_bp
from .order_route import order_bp
from .order_detail_route import order_detail_bp

def register_blueprints(app):
    app.register_blueprint(customer_bp, url_prefix="/customers")
    app.register_blueprint(sushi_item_bp, url_prefix="/sushi_items")
    app.register_blueprint(order_bp, url_prefix="/orders")
    app.register_blueprint(order_detail_bp, url_prefix="/order_details")

def create_app():
    app = Flask(__name__)
    Swagger(app)
    register_blueprints(app)

    return app