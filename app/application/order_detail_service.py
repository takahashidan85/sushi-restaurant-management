from app.infrastructure.repositories.order_detail_repo import OrderDetailRepository

class OrderDetailService:
    @staticmethod
    def create(order_id: int, sushi_item_id: int, quantity: int = 1):
        return OrderDetailRepository.add(order_id, sushi_item_id, quantity)

    @staticmethod
    def list_all():
        return OrderDetailRepository.list_all()

    @staticmethod
    def get(od_id: int):
        return OrderDetailRepository.get(od_id)

    @staticmethod
    def update(od_id: int, quantity: int | None):
        return OrderDetailRepository.update(od_id, quantity)

    @staticmethod
    def delete(od_id: int) -> bool:
        return OrderDetailRepository.delete(od_id)
