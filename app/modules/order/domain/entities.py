from datetime import datetime

class Order:
    """Order entity."""

    def __init__(self, id: int | None, customer_id: int, order_type: str, status: str | None = None, create_time: datetime | None = None, total_price: int = 0):
        self.id = id
        self.customer_id = customer_id
        self.order_type = order_type
        self.status = status
        self.create_time = create_time
        self.total_price = total_price

