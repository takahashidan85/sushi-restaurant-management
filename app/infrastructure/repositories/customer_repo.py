from app.extensions import db
from app.infrastructure.models.customer_models import CustomerModel

class CustomerRepository:
    @staticmethod
    def add(name: str, email: str) -> CustomerModel:
        c = CustomerModel(name=name, email=email)
        db.session.add(c)
        db.session.commit()
        return c

    @staticmethod
    def list_all() -> list[CustomerModel]:
        return CustomerModel.query.all()

    @staticmethod
    def get(customer_id: int) -> CustomerModel | None:
        return CustomerModel.query.get(customer_id)

    @staticmethod
    def update(customer_id: int, name: str | None, email: str | None) -> CustomerModel | None:
        c = CustomerModel.query.get(customer_id)
        if not c:
            return None
        if name:
            c.name = name
        if email:
            c.email = email
        db.session.commit()
        return c

    @staticmethod
    def delete(customer_id: int) -> bool:
        c = CustomerModel.query.get(customer_id)
        if not c:
            return False
        db.session.delete(c)
        db.session.commit()
        return True
