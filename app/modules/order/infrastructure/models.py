from app.core.extensions import db

class OrderModel(db.Model):
    """ORM model for the orders table."""

    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey("customers.id"), nullable=False)
    order_type = db.Column(db.String(50), nullable=False, default="dine-in")
    status = db.Column(db.String(50), nullable=False, default="pending")

    customer = db.relationship("CustomerModel", back_populates="orders")
    order_details = db.relationship("OrderDetailModel", back_populates="order", cascade="all, delete-orphan")
