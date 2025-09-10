from app.core.extensions import db

class SushiItemModel(db.Model):
    """ORM model for the sushi_items table."""

    __tablename__ = "sushi_items"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False, default=0)
    category = db.Column(db.String(50), nullable=True)
    description = db.Column(db.String(255), nullable=True)

    order_details = db.relationship("OrderDetailModel", back_populates="sushi_item", cascade="all, delete-orphan")

