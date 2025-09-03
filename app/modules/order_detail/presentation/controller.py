from flask import Blueprint, request
from marshmallow import ValidationError
from app.core.responses import success_response, error_response
from ..application.service import OrderDetailService
from .schema import OrderDetailCreateSchema, OrderDetailUpdateSchema, OrderDetailResponseSchema

bp = Blueprint("order_detail", __name__, url_prefix="/order-details")

create_schema = OrderDetailCreateSchema()
update_schema = OrderDetailUpdateSchema()
response_schema = OrderDetailResponseSchema()
response_list_schema = OrderDetailResponseSchema(many=True)

@bp.route("", methods=["POST"])
def create_order_detail():
    try:
        data = create_schema.load(request.get_json() or {})
        od = OrderDetailService.create(**data)
        return success_response(response_schema.dump(od), "Order detail created", 201)
    except ValidationError as err:
        return error_response("Validation Error", 422, err.messages)

@bp.route("", methods=["GET"])
def list_order_details():
    ods = OrderDetailService.list_all()
    return success_response(response_list_schema.dump(ods), "Order details retrieved", 200)

@bp.route("<int:od_id>", methods=["GET"])
def get_order_detail(od_id):
    od = OrderDetailService.get(od_id)
    return success_response(response_schema.dump(od), "Order detail retrieved", 200)

@bp.route("<int:od_id>", methods=["PUT"])
def update_order_detail(od_id):
    try:
        data = update_schema.load(request.get_json() or {})
        od = OrderDetailService.update(od_id, **data)
        return success_response(response_schema.dump(od), "Order detail updated", 200)
    except ValidationError as err:
        return error_response("Validation Error", 422, err.messages)

@bp.route("<int:od_id>", methods=["DELETE"])
def delete_order_detail(od_id):
    OrderDetailService.delete(od_id)
    return success_response(None, "Order detail deleted", 200)
