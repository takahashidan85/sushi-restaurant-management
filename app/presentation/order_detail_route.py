from flask import Blueprint, request, jsonify
from app.application.order_detail_service import OrderDetailService

order_detail_bp = Blueprint("order_details", __name__)

@order_detail_bp.post("/")
def create_order_detail():
    """
    Create a new order detail
    ---
    tags:
      - Order Details
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required: [order_id, sushi_item_id]
          properties:
            order_id:
              type: integer
            sushi_item_id:
              type: integer
            quantity:
              type: integer
              default: 1
    responses:
      201:
        description: Order detail created successfully
        examples:
          application/json: {"id":1,"order_id":1,"sushi_item_id":2,"quantity":3}
      400:
        description: order_id and sushi_item_id required
    """
    data = request.get_json() or {}
    order_id = data.get("order_id")
    sushi_item_id = data.get("sushi_item_id")
    quantity = data.get("quantity", 1)
    if not order_id or not sushi_item_id:
        return {"error": "order_id and sushi_item_id required"}, 400
    od = OrderDetailService.create(order_id, sushi_item_id, quantity)
    return jsonify(od.to_dict()), 201

@order_detail_bp.get("/")
def list_order_details():
    """
    Get all order details
    ---
    tags:
      - Order Details
    responses:
      200:
        description: List of order details
        examples:
          application/json: [{"id":1,"order_id":1,"sushi_item_id":2,"quantity":3}]
    """
    details = OrderDetailService.list_all()
    return jsonify([d.to_dict() for d in details])

@order_detail_bp.get("/<int:od_id>")
def get_order_detail(od_id):
    """
    Get order detail by ID
    ---
    tags:
      - Order Details
    parameters:
      - in: path
        name: od_id
        type: integer
        required: true
    responses:
      200:
        description: Order detail found
        examples:
          application/json: {"id":1,"order_id":1,"sushi_item_id":2,"quantity":3}
      404:
        description: Order detail not found
    """
    od = OrderDetailService.get(od_id)
    if not od:
        return {"error": "not found"}, 404
    return jsonify(od.to_dict())

@order_detail_bp.put("/<int:od_id>")
def update_order_detail(od_id):
    """
    Update order detail
    ---
    tags:
      - Order Details
    parameters:
      - in: path
        name: od_id
        type: integer
        required: true
      - in: body
        name: body
        schema:
          type: object
          properties:
            quantity:
              type: integer
    responses:
      200:
        description: Order detail updated
        examples:
          application/json: {"id":1,"order_id":1,"sushi_item_id":2,"quantity":5}
      404:
        description: Order detail not found
    """
    data = request.get_json() or {}
    od = OrderDetailService.update(od_id, data.get("quantity"))
    if not od:
        return {"error": "not found"}, 404
    return jsonify(od.to_dict())

@order_detail_bp.delete("/<int:od_id>")
def delete_order_detail(od_id):
    """
    Delete order detail
    ---
    tags:
      - Order Details
    parameters:
      - in: path
        name: od_id
        type: integer
        required: true
    responses:
      200:
        description: Order detail deleted
        examples:
          application/json: {"message": "deleted"}
      404:
        description: Order detail not found
    """
    if not OrderDetailService.delete(od_id):
        return {"error": "not found"}, 404
    return {"message": "deleted"}
