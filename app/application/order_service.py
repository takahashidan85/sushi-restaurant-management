from app.extensions import db
from app.infrastructure.models import define_models

def init():
    return define_models(db)

class OrderService:
    @staticmethod
    def create_order(table_number: int = None):
        models = init()
        Order = models['Order']
        o = Order(table_number=table_number)
        db.session.add(o)
        db.session.commit()
        return o

    @staticmethod
    def add_item(order_id: int, menu_item_id: int, quantity: int = 1):
        models = init()
        Order = models['Order']
        OrderItem = models['OrderItem']
        o = Order.query.get(order_id)
        if not o:
            return None
        oi = OrderItem(order_id=order_id, menu_item_id=menu_item_id, quantity=quantity)
        db.session.add(oi)
        db.session.commit()
        # recalc
        o.recalc_total(db)
        db.session.commit()
        return o
