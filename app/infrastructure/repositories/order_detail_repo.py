from app.extensions import db
from app.infrastructure.models.order_detail_models import OrderDetailModel

class OrderDetailRepository:
    @staticmethod
    def add(order_id: int, sushi_item_id: int, quantity: int = 1) -> OrderDetailModel:
        od = OrderDetailModel(order_id=order_id, sushi_item_id=sushi_item_id, quantity=quantity)
        db.session.add(od)
        db.session.commit()
        return od

    @staticmethod
    def list_all() -> list[OrderDetailModel]:
        return OrderDetailModel.query.all()

    @staticmethod
    def get(od_id: int) -> OrderDetailModel | None:
        return OrderDetailModel.query.get(od_id)

    @staticmethod
    def update(od_id: int, quantity: int | None) -> OrderDetailModel | None:
        od = OrderDetailModel.query.get(od_id)
        if not od:
            return None
        if quantity is not None:
            od.quantity = quantity
        db.session.commit()
        return od

    @staticmethod
    def delete(od_id: int) -> bool:
        od = OrderDetailModel.query.get(od_id)
        if not od:
            return False
        db.session.delete(od)
        db.session.commit()
        return True
