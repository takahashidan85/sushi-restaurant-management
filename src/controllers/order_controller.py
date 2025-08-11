from flask import Blueprint, jsonify, request

order_bp = Blueprint("order", __name__)
orders = []

@order_bp.route("/", methods=["GET"])
def get_orders():
    return jsonify(orders)

@order_bp.route("/", methods=["POST"])
def create_order():
    data = request.json
    orders.append(data)
    return jsonify({"message": "Order created"}), 201
