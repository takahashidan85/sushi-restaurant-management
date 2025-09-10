from ..infrastructure.repository import OrderDetailRepository
from ..domain.exceptions import InvalidOrderDetailDataError
from app.modules.order.application.service import OrderService

class OrderDetailService:
    @staticmethod
    def create(order_id: int, sushi_item_id: int, quantity: int):
        if quantity <= 0:
            raise InvalidOrderDetailDataError("Quantity must be greater than zero.")
        OrderService.update_total(order_id)
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
        detail = OrderDetailRepository.update(order_detail_id, quantity)
        if detail:
            OrderService.update_total(detail.order_id)
        return detail
    
    @staticmethod
    def delete(order_detail_id: int):
        order_id = OrderDetailRepository.get_order_id(order_detail_id)
        deleted = OrderDetailRepository.delete(order_detail_id)
        if deleted and order_id:
            OrderService.update_total(order_id)
        return deleted
