from ..infrastructure.repository import SushiItemRepository
from ..domain.exceptions import SushiItemAlreadyExistsError

class SushiItemService:
    @staticmethod
    def create(name, price, category=None, description=None):
        from ..infrastructure.models import SushiItemModel
        existing = SushiItemModel.query.filter_by(name=name).first()
        if existing:
            raise SushiItemAlreadyExistsError(f"Sushi item '{name}' already exists")
        return SushiItemRepository.add(name, price, category, description)

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
