from flask import Blueprint, jsonify, request

menu_bp = Blueprint("menu", __name__)
menu_items = [
    {"id": 1, "name": "Sushi cá hồi", "price": 50000},
    {"id": 2, "name": "Sushi tôm", "price": 60000},
]

@menu_bp.route("/", methods=["GET"])
def get_menu():
    return jsonify(menu_items)

@menu_bp.route("/", methods=["POST"])
def add_menu_item():
    data = request.json
    new_id = max(item["id"] for item in menu_items) + 1 if menu_items else 1
    data["id"] = new_id
    menu_items.append(data)
    return jsonify({"message": "Menu item added"}), 201
