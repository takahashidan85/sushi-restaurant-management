from app.extensions import db

class OrderDetail(db.Model):
    __tablename__ = "order_details"

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey("orders.id"), nullable=False)
    sushi_item_id = db.Column(db.Integer, db.ForeignKey("sushi_items.id"), nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=1)

    order = db.relationship("Order", back_populates="order_details")
    sushi_item = db.relationship("SushiItem", back_populates="order_details")

    def to_dict(self):
        return {
            "id": self.id,
            "order_id": self.order_id,
            "sushi_item_id": self.sushi_item_id,
            "quantity": self.quantity,
        }
