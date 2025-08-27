from flask import Blueprint, request, jsonify
from app.application.menu_service import MenuService

bp = Blueprint('menu', __name__)

@bp.post('/')
def create_menu():
    data = request.get_json() or {}
    name = data.get('name')
    price = data.get('price')
    category = data.get('category')
    if not name or price is None:
        return {'error': 'name and price required'}, 400
    m = MenuService.create(name, float(price), category)
    return jsonify(m.to_dict()), 201

@bp.get('/')
def list_menu():
    items = MenuService.list_all()
    return jsonify([i.to_dict() for i in items])

@bp.get('/<int:item_id>')
def get_menu(item_id):
    m = MenuService.get(item_id)
    if not m:
        return {'error': 'not found'}, 404
    return jsonify(m.to_dict())
