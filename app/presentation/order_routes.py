from flask import Blueprint, request, jsonify
from app.application.order_service import OrderService

bp = Blueprint('orders', __name__)

@bp.post('/')
def create_order():
    data = request.get_json() or {}
    table_number = data.get('table_number')
    o = OrderService.create_order(table_number=table_number)
    return jsonify({'id': o.id, 'table_number': o.table_number, 'total': o.total}), 201

@bp.post('/<int:order_id>/items')
def add_item(order_id):
    data = request.get_json() or {}
    menu_item_id = data.get('menu_item_id')
    quantity = data.get('quantity', 1)
    o = OrderService.add_item(order_id, menu_item_id, quantity)
    if not o:
        return {'error': 'order not found'}, 404
    return jsonify({'id': o.id, 'total': o.total})
