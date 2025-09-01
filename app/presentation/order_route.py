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

@order_bp.get("/<int:order_id>/details")
def get_order_details(order_id):
    """
    Get all order details for a specific order
    ---
    tags:
      - Orders
    parameters:
      - in: path
        name: order_id
        type: integer
        required: true
        description: ID of the order to retrieve details for
    responses:
      200:
        description: List of order details for the order
        examples:
          application/json: 
            - {"id":1,"order_id":1,"sushi_item_id":2,"quantity":3}
            - {"id":2,"order_id":1,"sushi_item_id":5,"quantity":1}
      404:
        description: Order not found
    """
    from app.application.order_detail_service import OrderDetailService
    details = OrderDetailService.list_by_order(order_id)
    if details is None:
        return {"error": "order not found"}, 404
    return jsonify([d.to_dict() for d in details])

@order_bp.put("/<int:order_id>")
def update_order(order_id):
    """
    Update an order
    ---
    tags:
      - Orders
    parameters:
      - in: path
        name: order_id
        type: integer
        required: true
        description: ID of the order to update
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            customer_id:
              type: integer
              description: New customer ID for the order
    responses:
      200:
        description: Order updated successfully
        examples:
          application/json: {"id":1,"customer_id":2,"status":"pending"}
      404:
        description: Order not found
    """
    data = request.get_json() or {}
    o = OrderService.update(order_id, data.get("customer_id"))
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
