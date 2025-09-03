from app.core.extensions import db

class CustomerModel(db.Model):
    """ORM model for the customers table."""

    __tablename__ = "customers"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    orders = db.relationship("OrderModel", back_populates="customer", cascade="all, delete-orphan")
