class OrderDetail:
    """OrderDetail entity."""
    
    def __init__(self, id: int | None, order_id: int, sushi_item_id: int, quantity: int = 1, total_price: float = 0.0):
        self.id = id
        self.order_id = order_id
        self.sushi_item_id = sushi_item_id
        self.quantity = quantity
        self.total_price = total_price
