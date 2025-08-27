from flask import Blueprint, request, jsonify
from app.application.order_service import OrderService

order_bp = Blueprint("orders", __name__)

@order_bp.post("/")
def create_order():
    """
    Create a new order
    ---
    tags:
      - Orders
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required: [customer_id]
          properties:
            customer_id:
              type: integer
    responses:
      201:
        description: Order created successfully
        examples:
          application/json: {"id":1,"customer_id":1,"status":"pending"}
      400:
        description: customer_id required
    """
    data = request.get_json() or {}
    customer_id = data.get("customer_id")
    if not customer_id:
        return {"error": "customer_id required"}, 400
    o = OrderService.create(customer_id)
    return jsonify(o.to_dict()), 201

@order_bp.get("/")
def list_orders():
    """
    Get all orders
    ---
    tags:
      - Orders
    responses:
      200:
        description: List of orders
        examples:
          application/json: [{"id":1,"customer_id":1,"status":"pending"}]
    """
    orders = OrderService.list_all()
    return jsonify([o.to_dict() for o in orders])

@order_bp.get("/<int:order_id>")
def get_order(order_id):
    """
    Get order by ID
    ---
    tags:
      - Orders
    parameters:
      - in: path
        name: order_id
        type: integer
        required: true
    responses:
      200:
        description: Order found
        examples:
          application/json: {"id":1,"customer_id":1,"status":"pending"}
      404:
        description: Order not found
    """
    o = OrderService.get(order_id)
    if not o:
        return {"error": "not found"}, 404
    return jsonify(o.to_dict())

@order_bp.delete("/<int:order_id>")
def delete_order(order_id):
    """
    Delete an order
    ---
    tags:
      - Orders
    parameters:
      - in: path
        name: order_id
        type: integer
        required: true
    responses:
      200:
        description: Order deleted successfully
        examples:
          application/json: {"message": "deleted"}
      404:
        description: Order not found
    """
    if not OrderService.delete(order_id):
        return {"error": "not found"}, 404
    return {"message": "deleted"}
