from app.core.extensions import db
from .models import OrderModel
from ..domain.entities import Order
from ..domain.exceptions import OrderNotFoundError

class OrderRepository:
    """Repository for Order persistence operations."""

    @staticmethod
    def _to_entity(model: OrderModel) -> Order:
        return Order(model.id, model.customer_id, model.order_type, model.status)

    @staticmethod
    def add(customer_id: int, order_type: str) -> Order:
        o = OrderModel(customer_id=customer_id, order_type=order_type, status="pending")
        db.session.add(o)
        db.session.commit()
        return OrderRepository._to_entity(o)

    @staticmethod
    def list_all() -> list[Order]:
        orders = OrderModel.query.all()
        return [OrderRepository._to_entity(o) for o in orders]

    @staticmethod
    def get(order_id: int) -> Order | None:
        o = OrderModel.query.get(order_id)
        if not o:
            raise OrderNotFoundError(f"Order with ID {order_id} not found.")
        return OrderRepository._to_entity(o)

    @staticmethod
    def update(order_id: int, customer_id: int | None) -> Order | None:
        o = OrderModel.query.get(order_id)
        if not o:
            raise OrderNotFoundError(f"Order with ID {order_id} not found.")
        
        if customer_id:
            o.customer_id = customer_id
        
        db.session.commit()
        return OrderRepository._to_entity(o)
    
    @staticmethod
    def update_status(order_id: int, new_status: str) -> Order:
        o = OrderModel.query.get(order_id)
        if not o:
            raise OrderNotFoundError(f"Order with ID {order_id} not found.")
        o.status = new_status
        db.session.commit()
        return OrderRepository._to_entity(o)

    @staticmethod
    def delete(order_id: int) -> bool:
        o = OrderModel.query.get(order_id)
        if not o:
            raise OrderNotFoundError(f"Order with ID {order_id} not found.")
        
        db.session.delete(o)
        db.session.commit()
        return True
