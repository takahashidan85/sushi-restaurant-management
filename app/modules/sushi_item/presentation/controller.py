from flask import Blueprint, request
from marshmallow import ValidationError
from app.core.responses import success_response, error_response
from ..application.service import SushiItemService
from ..domain.exceptions import SushiItemAlreadyExistsError
from .schema import SushiItemCreateSchema, SushiItemUpdateSchema, SushiItemResponseSchema

bp = Blueprint('sushi_item', __name__, url_prefix='/sushi-items')

create_schema = SushiItemCreateSchema()
update_schema = SushiItemUpdateSchema()
response_schema = SushiItemResponseSchema()
response_list_schemas = SushiItemResponseSchema(many=True)

@bp.route('', methods=['POST'])
def create_sushi_item():
    """Create a new sushi item."""
    try:
        data = create_schema.load(request.get_json() or {})
        item = SushiItemService.create(**data)
        return success_response(response_schema.dump(item), "Sushi item created", 201)
    except ValidationError as err:
        return error_response("Validation Error", 400, err.messages)
    except SushiItemAlreadyExistsError as err:
        return error_response(str(err), 409)
    
@bp.route('', methods=['GET'])
def list_sushi_items():
    """List all sushi items."""
    items = SushiItemService.list_all()
    return success_response(response_list_schemas.dump(items), "Sushi items retrieved", 200)

@bp.route('<int:item_id>', methods=['GET'])
def get_sushi_item(item_id):
    """Get a sushi item by ID."""
    item = SushiItemService.get(item_id)
    return success_response(response_schema.dump(item), "Sushi item retrieved", 200)

@bp.route('<int:item_id>', methods=['PUT'])
def update_sushi_item(item_id):
    """Update a sushi item by ID."""
    try:
        data = update_schema.load(request.get_json() or {})
        item = SushiItemService.update(item_id, **data)
        return success_response(response_schema.dump(item), "Sushi item updated", 200)
    except ValidationError as err:
        return error_response("Validation Error", 400, err.messages)
    
@bp.route('<int:item_id>', methods=['DELETE'])
def delete_sushi_item(item_id):
    """Delete a sushi item by ID."""
    SushiItemService.delete(item_id)
    return success_response(None, "Sushi item deleted", 200)