from app.extensions import db

class OrderModel(db.Model):
    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey("customers.id"), nullable=False)

    customer = db.relationship("CustomerModel", back_populates="orders")
    order_details = db.relationship("OrderDetailModel", back_populates="order", cascade="all, delete-orphan")

    def to_dict(self, include_details: bool = True):
        data = {"id": self.id, "customer_id": self.customer_id}
        if include_details:
            data["order_details"] = [d.to_dict() for d in self.order_details]
        return data
