from flask import Blueprint, request, jsonify
from app.application.customer_service import CustomerService

customer_bp = Blueprint("customers", __name__)

@customer_bp.post("/")
def create_customer():
    data = request.get_json() or {}
    name, email = data.get("name"), data.get("email")
    if not name or not email:
        return {"error": "name and email required"}, 400
    c = CustomerService.create(name, email)
    return jsonify(c.to_dict()), 201

@customer_bp.get("/")
def list_customers():
    customers = CustomerService.list_all()
    return jsonify([c.to_dict() for c in customers])

@customer_bp.get("/<int:customer_id>")
def get_customer(customer_id):
    c = CustomerService.get(customer_id)
    if not c:
        return {"error": "not found"}, 404
    return jsonify(c.to_dict())

@customer_bp.put("/<int:customer_id>")
def update_customer(customer_id):
    data = request.get_json() or {}
    c = CustomerService.update(customer_id, data.get("name"), data.get("email"))
    if not c:
        return {"error": "not found"}, 404
    return jsonify(c.to_dict())

@customer_bp.delete("/<int:customer_id>")
def delete_customer(customer_id):
    if not CustomerService.delete(customer_id):
        return {"error": "not found"}, 404
    return {"message": "deleted"}
