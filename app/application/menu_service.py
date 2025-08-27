from app.extensions import db
from app.infrastructure.models import define_models

models = {}

def init_models():
    global models
    if not models:
        models = define_models(db)
    return models

class MenuService:
    @staticmethod
    def create(name: str, price: float, category: str = None):
        m = init_models()['MenuItem'](name=name, price=price, category=category)
        db.session.add(m)
        db.session.commit()
        return m

    @staticmethod
    def list_all():
        MenuItem = init_models()['MenuItem']
        return MenuItem.query.order_by(MenuItem.id).all()

    @staticmethod
    def get(item_id: int):
        MenuItem = init_models()['MenuItem']
        return MenuItem.query.get(item_id)
