from flask import Blueprint, request, jsonify
from app.application.sushi_item_service import SushiItemService

sushi_item_bp = Blueprint("sushi_items", __name__)

@sushi_item_bp.post("/")
def create_sushi_item():
    data = request.get_json() or {}
    name = data.get("name")
    price = data.get("price")
    category = data.get("category")
    if not name or price is None:
        return {"error": "name and price required"}, 400
    item = SushiItemService.create(name, price, category)
    return jsonify(item.to_dict()), 201

@sushi_item_bp.get("/")
def list_sushi_items():
    items = SushiItemService.list_all()
    return jsonify([i.to_dict() for i in items])

@sushi_item_bp.get("/<int:item_id>")
def get_sushi_item(item_id):
    item = SushiItemService.get(item_id)
    if not item:
        return {"error": "not found"}, 404
    return jsonify(item.to_dict())

@sushi_item_bp.put("/<int:item_id>")
def update_sushi_item(item_id):
    data = request.get_json() or {}
    item = SushiItemService.update(
        item_id,
        name=data.get("name"),
        price=data.get("price"),
        category=data.get("category"),
    )
    if not item:
        return {"error": "not found"}, 404
    return jsonify(item.to_dict())

@sushi_item_bp.delete("/<int:item_id>")
def delete_sushi_item(item_id):
    success = SushiItemService.delete(item_id)
    if not success:
        return {"error": "not found"}, 404
    return {"message": "deleted"}
