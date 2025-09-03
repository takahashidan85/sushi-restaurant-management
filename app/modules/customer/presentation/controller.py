from flask import Blueprint, request
from marshmallow import ValidationError
from app.core.responses import success_response, error_response
from ..application.service import CustomerService
from .schema import CustomerCreateSchema, CustomerUpdateSchema, CustomerResponseSchema

bp = Blueprint('customer', __name__, url_prefix='/customers')

create_schema = CustomerCreateSchema()
update_schema = CustomerUpdateSchema()
response_schema = CustomerResponseSchema()
response_list_schema = CustomerResponseSchema(many=True)

@bp.route('', methods=['POST'])
def create_customer():
    """Create a new customer."""
    try:
        data = create_schema.load(request.get_json() or {})
        customer = CustomerService.create(**data)
        return success_response(response_schema.dump(customer), "Customer created", 201)
    except ValidationError as err:
        return error_response("Validation Error", 400, err.messages)
    
@bp.route('', methods=['GET'])
def list_customers():
    """List all customers."""
    customers = CustomerService.list_all()
    return success_response(response_list_schema.dump(customers), "Customers retrieved", 200)

@bp.route('<int:customer_id>', methods=['GET'])
def get_customer(customer_id):
    """Get a customer by ID."""
    customer = CustomerService.get(customer_id)
    return success_response(response_schema.dump(customer), "Customer retrieved", 200)

@bp.route('<int:customer_id>', methods=['PUT'])
def update_customer(customer_id):
    """Update a customer by ID."""
    try:
        data = update_schema.load(request.get_json() or {})
        customer = CustomerService.update(customer_id, **data)
        return success_response(response_schema.dump(customer), "Customer updated", 200)
    except ValidationError as err:
        return error_response("Validation Error", 400, err.messages)
    
@bp.route('<int:customer_id>', methods=['DELETE'])
def delete_customer(customer_id):
    """Delete a customer by ID."""
    CustomerService.delete(customer_id)
    return success_response(None, "Customer deleted", 200)