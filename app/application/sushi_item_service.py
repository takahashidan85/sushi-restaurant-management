from app.infrastructure.repositories.sushi_item_repo import SushiItemRepository

class SushiItemService:
    @staticmethod
    def create(name, price, category=None, description=None):
        return SushiItemRepository.add(name, float(price), category, description)

    @staticmethod
    def list_all():
        return SushiItemRepository.list_all()

    @staticmethod
    def get(item_id: int):
        return SushiItemRepository.get(item_id)

    @staticmethod
    def update(item_id: int, name=None, price=None, category=None, description=None):
        return SushiItemRepository.update(item_id, name, price, category, description)

    @staticmethod
    def delete(item_id: int) -> bool:
        return SushiItemRepository.delete(item_id)
