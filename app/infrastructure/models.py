from . import db  # will be monkey-patched in package import
from datetime import datetime

# NOTE: We will import db from app.extensions at runtime; this placeholder prevents static import errors.
# Actual models use the db object from app.extensions.

# However, to keep this module standalone, define models using a factory function below.
def define_models(db):
    class MenuItem(db.Model):
        __tablename__ = 'menu_items'
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(128), nullable=False)
        price = db.Column(db.Float, nullable=False)
        category = db.Column(db.String(64), nullable=True)
        created_at = db.Column(db.DateTime, default=datetime.utcnow)

        def to_dict(self):
            return {'id': self.id, 'name': self.name, 'price': self.price, 'category': self.category}

    class OrderItem(db.Model):
        __tablename__ = 'order_items'
        id = db.Column(db.Integer, primary_key=True)
        order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
        menu_item_id = db.Column(db.Integer, db.ForeignKey('menu_items.id'), nullable=False)
        quantity = db.Column(db.Integer, nullable=False, default=1)

    class Order(db.Model):
        __tablename__ = 'orders'
        id = db.Column(db.Integer, primary_key=True)
        table_number = db.Column(db.Integer, nullable=True)
        status = db.Column(db.String(32), default='open')
        total = db.Column(db.Float, default=0.0)
        created_at = db.Column(db.DateTime, default=datetime.utcnow)
        items = db.relationship('OrderItem', backref='order', cascade='all, delete-orphan')

        def recalc_total(self, db):
            total = 0.0
            for oi in self.items:
                menu = db.session.get(MenuItem, oi.menu_item_id)
                if menu:
                    total += (menu.price or 0.0) * oi.quantity
            self.total = total

    class Reservation(db.Model):
        __tablename__ = 'reservations'
        id = db.Column(db.Integer, primary_key=True)
        customer_name = db.Column(db.String(128), nullable=False)
        table_number = db.Column(db.Integer, nullable=False)
        reserved_at = db.Column(db.DateTime, nullable=False)

    class Staff(db.Model):
        __tablename__ = 'staff'
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(128), nullable=False)
        role = db.Column(db.String(32), nullable=False)

    return {
        'MenuItem': MenuItem,
        'Order': Order,
        'OrderItem': OrderItem,
        'Reservation': Reservation,
        'Staff': Staff,
    }
