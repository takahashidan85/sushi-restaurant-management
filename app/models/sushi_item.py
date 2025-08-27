from app.extensions import db

class SushiItem(db.Model):
    __tablename__ = "sushi_items"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

    order_details = db.relationship("OrderDetail", back_populates="sushi_item")

    def to_dict(self):
        return {"id": self.id, "name": self.name, "price": self.price}
