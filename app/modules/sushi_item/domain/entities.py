class SushiItem:
    """SushiItem entity."""

    def __init__(self, id: int | None, name: str, price: int = 0, category: str | None = None, description: str | None = None):
        self.id = id
        self.name = name
        self.price = price
        self.category = category
        self.description = description
