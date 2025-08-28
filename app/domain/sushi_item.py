class SushiItem:
    def __init__(self, id: int | None, name: str, price: float, category: str | None = None, description: str | None = None):
        self.id = id
        self.name = name
        self.price = price
        self.category = category
        self.description = description
