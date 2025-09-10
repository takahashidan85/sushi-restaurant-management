from app.core.extensions import db
from datetime import datetime
import pytz

class OrderModel(db.Model):
    """ORM model for the orders table."""

    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey("customers.id"), nullable=False)
    order_type = db.Column(db.String(50), nullable=False, default="dine_in")
    status = db.Column(db.String(50), nullable=False, default="pending")
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    total_price = db.Column(db.Integer, default=0)

    customer = db.relationship("CustomerModel", back_populates="orders")
    order_details = db.relationship("OrderDetailModel", back_populates="order", cascade="all, delete-orphan")


