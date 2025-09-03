from ..infrastructure.repository import OrderRepository
from ..domain.exceptions import OrderNotFoundError, OrderInvalidStatusError, OrderStatusConflictError

class OrderService:
    """Service layer for Order operations."""
    
    STATUS_FLOW = {
        "dine-in": ["pending", "preparing", "ready", "served", "completed", "cancelled"],
        "take_out": ["pending", "preparing", "ready", "completed", "cancelled"],
        "delivery": ["pending", "preparing", "ready", "delivering", "completed", "cancelled"]
    }

    @staticmethod
    def create(customer_id: int, order_type: str):
        if order_type not in ["dine-in", "take_out", "delivery"]:
            raise OrderInvalidStatusError(f"Invalid order type: {order_type}")
        return OrderRepository.add(customer_id, order_type)

    @staticmethod
    def list_all():
        return OrderRepository.list_all()
    
    @staticmethod
    def get(order_id: int):
        return OrderRepository.get(order_id)

    @staticmethod
    def update(order_id: int, customer_id: int | None):
        return OrderRepository.update(order_id, customer_id)
    
    @staticmethod
    def update_status(order_id: int, new_status: str):
        order = OrderRepository.get(order_id)
        allowed_status = OrderService.STATUS_FLOW.get(order.order_type, [])

        if new_status not in allowed_status:
            """When the new status is not in the allowed flow."""
            raise OrderInvalidStatusError(f"Invalid status '{new_status}' for order type '{order.order_type}'")

        current_index = allowed_status.index(order.status)
        new_index = allowed_status.index(new_status)

        if new_index < current_index and new_status != "cancelled":
            """No rollback allowed except to 'cancelled'."""
            raise OrderStatusConflictError(f"Cannot change status from '{order.status}' to '{new_status}'")
        
        return OrderRepository.update_status(order_id, new_status)
    
    @staticmethod
    def force_update_status(order_id: int, new_status: str):
        """Force update status without validation."""
        """Admin use only."""
        order = OrderRepository.get(order_id)
        allowed_status = OrderService.STATUS_FLOW.get(order.order_type, [])

        if new_status not in allowed_status:
            raise OrderInvalidStatusError(f"Invalid status '{new_status}' for order type '{order.order_type}'")
        
        return OrderRepository.update_status(order_id, new_status)
    
    @staticmethod
    def delete(order_id: int):
        return OrderRepository.delete(order_id)