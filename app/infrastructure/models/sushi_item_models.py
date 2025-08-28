from app.extensions import db

class SushiItemModel(db.Model):
    __tablename__ = "sushi_items"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), nullable=True)
    description = db.Column(db.String(255), nullable=True)

    order_details = db.relationship("OrderDetailModel", back_populates="sushi_item")

    def to_dict(self):
        return {"id": self.id, "name": self.name, "price": self.price, "category": self.category, "description": self.description}
