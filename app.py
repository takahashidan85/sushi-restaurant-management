from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models.customer import Customer
from models.sushi_item import SushiItem
from models.order import Order
from models.order_detail import OrderDetail

@app.route("/")
def index():
    return jsonify({"message": "Sushi Restaurant Management API is running!"})

if __name__ == "__main__":
    app.run(debug=True)
