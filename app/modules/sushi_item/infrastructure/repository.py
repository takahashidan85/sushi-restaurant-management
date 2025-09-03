from app.core.extensions import db
from .models import SushiItemModel
from ..domain.entities import SushiItem
from ..domain.exceptions import SushiItemNotFoundError

class SushiItemRepository:
    """Repository for SushiItem persistence operations."""

    @staticmethod
    def _to_entity(model: SushiItemModel) -> SushiItem:
        return SushiItem(model.id, model.name, model.price, model.category, model.description)
    
    @staticmethod
    def add(name: str, price: float, category: str, description: str | None) -> SushiItem:
        item = SushiItemModel(name=name, price=price, category=category, description=description)
        db.session.add(item)
        db.session.commit()
        return SushiItemRepository._to_entity(item)
    
    @staticmethod
    def list_all() -> list[SushiItem]:
        items = SushiItemModel.query.all()
        return [SushiItemRepository._to_entity(i) for i in items]
    
    @staticmethod
    def get(item_id: int) -> SushiItem | None:
        item = SushiItemModel.query.get(item_id)
        if not item:
            raise SushiItemNotFoundError(f"Sushi item with ID {item_id} not found.")
        return SushiItemRepository._to_entity(item)
    
    @staticmethod
    def update(item_id: int, name: str | None, price: float | None, category: str | None, description: str | None) -> SushiItem | None:
        item = SushiItemModel.query.get(item_id)
        if not item:
            raise SushiItemNotFoundError(f"Sushi item with ID {item_id} not found.")
        
        if name:
            item.name = name
        if price is not None:
            item.price = price
        if category:
            item.category = category
        if description is not None:
            item.description = description
        
        db.session.commit()
        return SushiItemRepository._to_entity(item)
    
    @staticmethod
    def delete(item_id: int) -> bool:
        item = SushiItemModel.query.get(item_id)
        if not item:
            raise SushiItemNotFoundError(f"Sushi item with ID {item_id} not found.")
        
        db.session.delete(item)
        db.session.commit()
        return True

