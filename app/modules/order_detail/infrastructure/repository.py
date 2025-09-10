from app.core.extensions import db
from ..infrastructure.models import OrderDetailModel
from app.modules.sushi_item.infrastructure.models import SushiItemModel
from ..domain.entities import OrderDetail
from ..domain.exceptions import OrderDetailNotFoundError

class OrderDetailRepository:
    """Repository for OrderDetail persistence operations."""

    @staticmethod
    def _to_entity(model: OrderDetailModel) -> OrderDetail:
        return OrderDetail(model.id, model.order_id, model.sushi_item_id, model.quantity, model.unit_price)
    
    @staticmethod
    def add(order_id: int, sushi_item_id: int, quantity: int = 1) -> OrderDetail:
        sushi_item = SushiItemModel.query.get(sushi_item_id)
        if not sushi_item:
            raise OrderDetailNotFoundError(f"Sushi item with ID {sushi_item_id} not found.")
        
        unit_price = sushi_item.price * quantity
        od = OrderDetailModel(order_id=order_id, sushi_item_id=sushi_item_id, quantity=quantity, unit_price=unit_price)
        db.session.add(od)
        db.session.commit()
        return OrderDetailRepository._to_entity(od)
    
    @staticmethod
    def list_all() -> list[OrderDetail]:
        return [OrderDetailRepository._to_entity(m) for m in OrderDetailModel.query.all()]
    
    @staticmethod
    def get(order_detail_id: int) -> OrderDetail:
        od = OrderDetailModel.query.get(order_detail_id)
        if not od:
            raise OrderDetailNotFoundError(f"Order detail with ID {order_detail_id} not found.")
        return OrderDetailRepository._to_entity(od)
    
    @staticmethod
    def list_by_order(order_id: int) -> list[OrderDetail]:
        ods = OrderDetailModel.query.filter_by(order_id=order_id).all()
        return [OrderDetailRepository._to_entity(m) for m in ods]
    
    @staticmethod
    def update(order_detail_id: int, quantity: int) -> OrderDetail:
        od = OrderDetailModel.query.get(order_detail_id)
        if not od:
            raise OrderDetailNotFoundError(f"Order detail with ID {order_detail_id} not found.")
        
        if quantity:
            od.quantity = quantity
            od.unit_price = od.sushi_item.price * quantity
        db.session.commit()
        return OrderDetailRepository._to_entity(od)

    @staticmethod
    def delete(order_detail_id: int) -> bool:
        od = OrderDetailModel.query.get(order_detail_id)
        if not od:
            raise OrderDetailNotFoundError(f"Order detail with ID {order_detail_id} not found.")
        
        db.session.delete(od)
        db.session.commit()
        return True