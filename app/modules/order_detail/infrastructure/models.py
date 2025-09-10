from app.core.extensions import db

class OrderDetailModel(db.Model):
    """ORM model for the order_details table."""

    __tablename__ = "order_details"

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey("orders.id"), nullable=False)
    sushi_item_id = db.Column(db.Integer, db.ForeignKey("sushi_items.id"), nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=1)
    unit_price = db.Column(db.Integer, nullable=False, default=0)

    order = db.relationship("OrderModel", back_populates="order_details")
    sushi_item = db.relationship("SushiItemModel", back_populates="order_details")

