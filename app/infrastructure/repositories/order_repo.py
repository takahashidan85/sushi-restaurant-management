from app.extensions import db
from app.infrastructure.models.order_models import OrderModel

class OrderRepository:
    @staticmethod
    def add(customer_id: int) -> OrderModel:
        o = OrderModel(customer_id=customer_id)
        db.session.add(o)
        db.session.commit()
        return o

    @staticmethod
    def list_all() -> list[OrderModel]:
        return OrderModel.query.all()

    @staticmethod
    def get(order_id: int) -> OrderModel | None:
        return OrderModel.query.get(order_id)
    
    @staticmethod
    def update(order_id: int, customer_id: int | None = None) -> OrderModel | None:
        o = OrderModel.query.get(order_id)
        if not o:
            return None
        if customer_id is not None:
            o.customer_id = customer_id
        db.session.commit()
        return o

    @staticmethod
    def delete(order_id: int) -> bool:
        o = OrderModel.query.get(order_id)
        if not o:
            return False
        db.session.delete(o)
        db.session.commit()
        return True
