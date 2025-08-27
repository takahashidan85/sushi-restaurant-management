from app.extensions import db

class Order(db.Model):
    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey("customers.id"), nullable=False)

    customer = db.relationship("Customer", back_populates="orders")
    order_details = db.relationship("OrderDetail", back_populates="order")

    def to_dict(self):
        return {"id": self.id, "customer_id": self.customer_id}
