from flask import Blueprint, request
from marshmallow import ValidationError
from app.core.responses import success_response, error_response
from ..application.service import OrderService
from .schema import OrderCreateSchema, OrderUpdateSchema, OrderStatusUpdateSchema, OrderResponseSchema

bp = Blueprint('order', __name__, url_prefix='/orders')

create_schema = OrderCreateSchema()
update_schema = OrderUpdateSchema()
status_schema = OrderStatusUpdateSchema()
response_schema = OrderResponseSchema()
response_list_schema = OrderResponseSchema(many=True)

@bp.route('', methods=['POST'])
def create_order():
    """Create a new order."""
    try:
        data = create_schema.load(request.get_json() or {})
        order = OrderService.create(**data)
        return success_response(response_schema.dump(order), "Order created", 201)
    except ValidationError as err:
        return error_response("Validation Error", 422, err.messages)
    
@bp.route('', methods=['GET'])
def list_orders():
    """List all orders."""
    orders = OrderService.list_all()
    return success_response(response_list_schema.dump(orders), "Orders retrieved", 200)

@bp.route('<int:order_id>', methods=['GET'])
def get_order(order_id):
    """Get an order by ID."""
    order = OrderService.get(order_id)
    return success_response(response_schema.dump(order), "Order retrieved", 200)

@bp.route('<int:order_id>', methods=['PUT'])
def update_order(order_id):
    """Update an order by ID."""
    try:
        data = update_schema.load(request.get_json() or {})
        order = OrderService.update(order_id, **data)
        return success_response(response_schema.dump(order), "Order updated", 200)
    except ValidationError as err:
        return error_response("Validation Error", 422, err.messages)
    
@bp.route('<int:order_id>/status', methods=['PATCH'])
def update_order_status(order_id):
    """Update the status of an order."""
    try:
        data = status_schema.load(request.get_json() or {})
        order = OrderService.update_status(order_id, data["new_status"])
        return success_response(response_schema.dump(order), "Order status updated", 200)
    except ValidationError as err:
        return error_response("Validation Error", 422, err.messages)
    
@bp.route('<int:order_id>/force-status', methods=['PATCH'])
def force_update_order_status(order_id):
    """Force update the status of an order (admin use only)."""
    try:
        data = status_schema.load(request.get_json() or {})
        order = OrderService.force_update_status(order_id, data["new_status"])
        return success_response(response_schema.dump(order), "Order status updated", 200)
    except ValidationError as err:
        return error_response("Validation Error", 422, err.messages)
    
@bp.route('<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    """Delete an order by ID."""
    OrderService.delete(order_id)
    return success_response(None, "Order deleted", 200)