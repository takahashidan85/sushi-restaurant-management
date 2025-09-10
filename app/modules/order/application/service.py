from ..infrastructure.repository import OrderRepository
from ..domain.exceptions import OrderInvalidStatusError, OrderStatusConflictError

class OrderService:
    """Service layer for Order operations."""
    
    STATUS_FLOW = {
        "dine_in": ["pending", "preparing", "ready", "served", "completed", "cancelled"],
        "take_out": ["pending", "preparing", "ready", "completed", "cancelled"],
        "delivery": ["pending", "preparing", "ready", "delivering", "completed", "cancelled"]
    }

    @staticmethod
    def create(customer_id: int, order_type: str):
        from app.modules.customer.infrastructure.models import CustomerModel
        from app.modules.customer.domain.exceptions import CustomerNotFoundError
        if order_type not in ["dine_in", "take_out", "delivery"]:
            raise OrderInvalidStatusError(f"Invalid order type: {order_type}")
        
        customer = CustomerModel.query.get(customer_id)
        """If the id doesn't exist."""
        if not customer:
            raise CustomerNotFoundError(f"Customer with id {customer_id} does not exist")
        
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
    def update_total(order_id: int):
        """Recalculate and update total price for an order"""
        order = OrderRepository.get(order_id)
        total = sum(d.quantity * d.sushi_item.price for d in order.order_details)

        return OrderRepository.update_total(order_id, total)
    
    @staticmethod
    def delete(order_id: int):
        return OrderRepository.delete(order_id)