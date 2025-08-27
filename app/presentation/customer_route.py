from flask import Blueprint, request, jsonify
from app.application.customer_service import CustomerService

customer_bp = Blueprint("customers", __name__)

@customer_bp.post("/")
def create_customer():
    """
    Create a new customer
    ---
    tags:
      - Customers
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - name
            - email
          properties:
            name:
              type: string
            email:
              type: string
    responses:
      201:
        description: Customer created successfully
        examples:
          application/json: {"id":1, "name":"Alice", "email":"alice@example.com"}
      400:
        description: Missing name or email
    """
    data = request.get_json() or {}
    name, email = data.get("name"), data.get("email")
    if not name or not email:
        return {"error": "name and email required"}, 400
    c = CustomerService.create(name, email)
    return jsonify(c.to_dict()), 201

@customer_bp.get("/")
def list_customers():
    """
    Get all customers
    ---
    tags:
      - Customers
    responses:
      200:
        description: List of customers
        examples:
          application/json: [{"id":1,"name":"Alice","email":"alice@example.com"}]
    """
    customers = CustomerService.list_all()
    return jsonify([c.to_dict() for c in customers])

@customer_bp.get("/<int:customer_id>")
def get_customer(customer_id):
    """
    Get customer by ID
    ---
    tags:
      - Customers
    parameters:
      - in: path
        name: customer_id
        type: integer
        required: true
    responses:
      200:
        description: Customer found
        examples:
          application/json: {"id":1,"name":"Alice","email":"alice@example.com"}
      404:
        description: Customer not found
    """
    c = CustomerService.get(customer_id)
    if not c:
        return {"error": "not found"}, 404
    return jsonify(c.to_dict())

@customer_bp.put("/<int:customer_id>")
def update_customer(customer_id):
    """
    Update customer
    ---
    tags:
      - Customers
    parameters:
      - in: path
        name: customer_id
        type: integer
        required: true
      - in: body
        name: body
        schema:
          type: object
          properties:
            name:
              type: string
            email:
              type: string
    responses:
      200:
        description: Customer updated
        examples:
          application/json: {"id":1,"name":"Alice Updated","email":"alice.new@example.com"}
      404:
        description: Customer not found
    """
    data = request.get_json() or {}
    c = CustomerService.update(customer_id, data.get("name"), data.get("email"))
    if not c:
        return {"error": "not found"}, 404
    return jsonify(c.to_dict())

@customer_bp.delete("/<int:customer_id>")
def delete_customer(customer_id):
    """
    Delete customer
    ---
    tags:
      - Customers
    parameters:
      - in: path
        name: customer_id
        type: integer
        required: true
    responses:
      200:
        description: Customer deleted
        examples:
          application/json: {"message": "deleted"}
      404:
        description: Customer not found
    """
    if not CustomerService.delete(customer_id):
        return {"error": "not found"}, 404
    return {"message": "deleted"}
