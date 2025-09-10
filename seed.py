from app.app_factory import create_app
from app.core.extensions import db
from app.modules.customer.infrastructure.models import CustomerModel
from app.modules.sushi_item.infrastructure.models import SushiItemModel
from app.modules.order.infrastructure.models import OrderModel
from app.modules.order_detail.infrastructure.models import OrderDetailModel

def run_seed():
    app = create_app()
    with app.app_context():
        print("Dropping all tables...")
        db.drop_all()
        print("Creating all tables...")
        db.create_all()

        """Seed Customers."""
        alice = CustomerModel(name="Alice", email="alice@example.com")
        bob = CustomerModel(name="Bob", email="bob@example.com")

        """Seed Sushi Item."""
        nigiri = SushiItemModel(name="Salmon Nigiri", price=50000, category="nigiri", description="Fresh salmon over rice")
        roll = SushiItemModel(name="Tuna Roll", price=60000, category="roll", description="Tuna wrapped in rice and seaweed")

        db.session.add_all([alice, bob, nigiri, roll])
        db.session.commit()

        """Seed Order."""
        order1 = OrderModel(customer_id=alice.id, order_type="dine_in", status="pending")
        db.session.add(order1)
        db.session.commit()

        """Seed Order Detail."""
        detail1 = OrderDetailModel(order_id=order1.id, sushi_item_id=nigiri.id, quantity=2)
        detail2 = OrderDetailModel(order_id=order1.id, sushi_item_id=roll.id, quantity=1)

        db.session.add_all([detail1, detail2])
        db.session.commit()


        order1.total_price = (
            detail1.quantity * nigiri.price +
            detail2.quantity * roll.price
        )
        db.session.commit()

        print("Seed completed.")

if __name__ == "__main__":
    run_seed()
