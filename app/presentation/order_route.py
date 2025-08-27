from flask import Blueprint, request, jsonify
from app.application.order_service import OrderService

order_bp = Blueprint("orders", __name__)

@order_bp.post("/")
def create_order():
    data = request.get_json() or {}
    customer_id = data.get("customer_id")
    if not customer_id:
        return {"error": "customer_id required"}, 400
    o = OrderService.create(customer_id)
    return jsonify(o.to_dict()), 201

@order_bp.get("/")
def list_orders():
    orders = OrderService.list_all()
    return jsonify([o.to_dict() for o in orders])

@order_bp.get("/<int:order_id>")
def get_order(order_id):
    o = OrderService.get(order_id)
    if not o:
        return {"error": "not found"}, 404
    return jsonify(o.to_dict())

@order_bp.delete("/<int:order_id>")
def delete_order(order_id):
    if not OrderService.delete(order_id):
        return {"error": "not found"}, 404
    return {"message": "deleted"}
