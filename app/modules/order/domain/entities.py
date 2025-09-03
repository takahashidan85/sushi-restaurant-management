class Order:
    """Order entity."""

    def __init__(self, id: int | None, customer_id: int, order_type: str, status: str | None = None):
        self.id = id
        self.customer_id = customer_id
        self.order_type = order_type
        self.status = status