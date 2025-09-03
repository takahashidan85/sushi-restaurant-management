from ..infrastructure.repository import OrderDetailRepository
from ..domain.exceptions import InvalidOrderDetailDataError

class OrderDetailService:
    @staticmethod
    def create(order_id: int, sushi_item_id: int, quantity: int):
        if quantity <= 0:
            raise InvalidOrderDetailDataError("Quantity must be greater than zero.")
        return OrderDetailRepository.add(order_id, sushi_item_id, quantity)
    
    @staticmethod
    def list_all():
        return OrderDetailRepository.list_all()
    
    @staticmethod
    def get(order_detail_id: int):
        return OrderDetailRepository.get(order_detail_id)
    
    @staticmethod
    def list_by_order(order_id: int):
        return OrderDetailRepository.list_by_order(order_id)
    
    @staticmethod
    def update(order_detail_id: int, quantity: int | None = None):
        if quantity is not None and quantity <= 0:
            raise InvalidOrderDetailDataError("Quantity must be greater than zero.")
        return OrderDetailRepository.update(order_detail_id, quantity)
    
    @staticmethod
    def delete(order_detail_id: int):
        return OrderDetailRepository.delete(order_detail_id)
