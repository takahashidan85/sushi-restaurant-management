from flask import Blueprint, request, jsonify
from app.application.sushi_item_service import SushiItemService

sushi_item_bp = Blueprint("sushi_items", __name__)

@sushi_item_bp.post("/")
def create_sushi_item():
    """
    Create a new sushi item
    ---
    tags:
      - Sushi Items
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required: [name, price]
          properties:
            name:
              type: string
            price:
              type: number
            category:
              type: string
            description:
              type: string
    responses:
      201:
        description: Sushi item created
        examples:
          application/json: {"id":1,"name":"Salmon Sushi","price":2.5,"category":"Nigiri","description":"Fresh salmon over rice"}
      400:
        description: Missing name or price
    """
    data = request.get_json() or {}
    name = data.get("name")
    price = data.get("price")
    category = data.get("category")
    description = data.get("description")
    if not name or price is None:
        return {"error": "name and price required"}, 400
    item = SushiItemService.create(name, price, category, description)
    return jsonify(item.to_dict()), 201

@sushi_item_bp.get("/")
def list_sushi_items():
    """
    Get all sushi items
    ---
    tags:
      - Sushi Items
    responses:
      200:
        description: List of sushi items
        examples:
          application/json: [{"id":1,"name":"Salmon Sushi","price":2.5,"category":"Nigiri","description":"Fresh salmon over rice"}]
    """
    items = SushiItemService.list_all()
    return jsonify([i.to_dict() for i in items])

@sushi_item_bp.get("/<int:item_id>")
def get_sushi_item(item_id):
    """
    Get a sushi item by ID
    ---
    tags:
      - Sushi Items
    parameters:
      - in: path
        name: item_id
        type: integer
        required: true
    responses:
      200:
        description: Sushi item found
        examples:
          application/json: {"id":1,"name":"Salmon Sushi","price":2.5,"category":"Nigiri","description":"Fresh salmon over rice"}
      404:
        description: Item not found
    """
    item = SushiItemService.get(item_id)
    if not item:
        return {"error": "not found"}, 404
    return jsonify(item.to_dict())

@sushi_item_bp.put("/<int:item_id>")
def update_sushi_item(item_id):
    """
    Update a sushi item
    ---
    tags:
      - Sushi Items
    parameters:
      - in: path
        name: item_id
        type: integer
        required: true
      - in: body
        name: body
        schema:
          type: object
          properties:
            name:
              type: string
            price:
              type: number
            category:
              type: string
            description:
              type: string
    responses:
      200:
        description: Sushi item updated
        examples:
          application/json: {"id":1,"name":"Updated Sushi","price":3.0,"category":"Roll","description":"Cucumber and avocado roll"}
      404:
        description: Item not found
    """
    data = request.get_json() or {}
    item = SushiItemService.update(
        item_id,
        name=data.get("name"),
        price=data.get("price"),
        category=data.get("category"),
        description=data.get("description"),
    )
    if not item:
        return {"error": "not found"}, 404
    return jsonify(item.to_dict())

@sushi_item_bp.delete("/<int:item_id>")
def delete_sushi_item(item_id):
    """
    Delete a sushi item
    ---
    tags:
      - Sushi Items
    parameters:
      - in: path
        name: item_id
        type: integer
        required: true
    responses:
      200:
        description: Sushi item deleted
        examples:
          application/json: {"message": "deleted"}
      404:
        description: Item not found
    """
    success = SushiItemService.delete(item_id)
    if not success:
        return {"error": "not found"}, 404
    return {"message": "deleted"}
