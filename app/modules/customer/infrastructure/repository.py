from app.core.extensions import db
from .models import CustomerModel
from ..domain.entities import Customer
from ..domain.exceptions import CustomerNotFoundError, CustomerAlreadyExistsError

class CustomerRepository:
    """Repository for Customer persistence operations."""

    @staticmethod
    def _to_entity(model: CustomerModel) -> Customer:
        return Customer(model.id, model.name, model.email)

    @staticmethod
    def add(name: str, email: str) -> Customer:
        if CustomerModel.query.filter_by(email=email).first():
            raise CustomerAlreadyExistsError(f"Customer with email {email} already exists.")
        
        c = CustomerModel(name=name, email=email)
        db.session.add(c)
        db.session.commit()
        return CustomerRepository._to_entity(c)

    @staticmethod
    def find_by_email(email: str) -> Customer | None:
        c = CustomerModel.query.filter_by(email=email).first()
        if c:
            return CustomerRepository._to_entity(c)
        return None
    
    @staticmethod
    def list_all() -> list[Customer]:
        customers = CustomerModel.query.all()
        return [CustomerRepository._to_entity(c) for c in customers]
    
    @staticmethod
    def get(customer_id: int) -> Customer | None:
        c = CustomerModel.query.get(customer_id)
        if not c:
            raise CustomerNotFoundError(f"Customer with ID {customer_id} not found.")
        return CustomerRepository._to_entity(c)
    
    @staticmethod
    def update(customer_id: int, name: str | None, email: str | None) -> Customer | None:
        c = CustomerModel.query.get(customer_id)
        if not c:
            raise CustomerNotFoundError(f"Customer with ID {customer_id} not found.")
        
        if email and email != c.email:
            if CustomerModel.query.filter_by(email=email).first():
                raise CustomerAlreadyExistsError(f"Customer with email {email} already exists.")
            c.email = email

        if name:
            c.name = name
        
        db.session.commit()
        return CustomerRepository._to_entity(c)
    
    @staticmethod
    def delete(customer_id: int) -> bool:
        c = CustomerModel.query.get(customer_id)
        if not c:
            raise CustomerNotFoundError(f"Customer with ID {customer_id} not found.")
        
        db.session.delete(c)
        db.session.commit()
        return True