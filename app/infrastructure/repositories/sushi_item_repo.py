from app.extensions import db
from app.infrastructure.models.sushi_item_models import SushiItemModel

class SushiItemRepository:
    @staticmethod
    def add(name: str, price: float, category: str | None = None, description: str | None = None) -> SushiItemModel:
        s = SushiItemModel(name=name, price=price, category=category, description=description)
        db.session.add(s)
        db.session.commit()
        return s

    @staticmethod
    def list_all() -> list[SushiItemModel]:
        return SushiItemModel.query.all()

    @staticmethod
    def get(item_id: int) -> SushiItemModel | None:
        return SushiItemModel.query.get(item_id)

    @staticmethod
    def update(item_id: int, name=None, price=None, category=None, description=None) -> SushiItemModel | None:
        s = SushiItemModel.query.get(item_id)
        if not s:
            return None
        if name is not None:
            s.name = name
        if price is not None:
            s.price = price
        if category is not None:
            s.category = category
        if description is not None:
            s.description = description
        db.session.commit()
        return s

    @staticmethod
    def delete(item_id: int) -> bool:
        s = SushiItemModel.query.get(item_id)
        if not s:
            return False
        db.session.delete(s)
        db.session.commit()
        return True
