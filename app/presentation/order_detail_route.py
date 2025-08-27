from flask import Blueprint, request, jsonify
from app.application.order_detail_service import OrderDetailService

order_detail_bp = Blueprint("order_details", __name__)

@order_detail_bp.post("/")
def create_order_detail():
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
    details = OrderDetailService.list_all()
    return jsonify([d.to_dict() for d in details])

@order_detail_bp.get("/<int:od_id>")
def get_order_detail(od_id):
    od = OrderDetailService.get(od_id)
    if not od:
        return {"error": "not found"}, 404
    return jsonify(od.to_dict())

@order_detail_bp.put("/<int:od_id>")
def update_order_detail(od_id):
    data = request.get_json() or {}
    od = OrderDetailService.update(od_id, data.get("quantity"))
    if not od:
        return {"error": "not found"}, 404
    return jsonify(od.to_dict())

@order_detail_bp.delete("/<int:od_id>")
def delete_order_detail(od_id):
    if not OrderDetailService.delete(od_id):
        return {"error": "not found"}, 404
    return {"message": "deleted"}
