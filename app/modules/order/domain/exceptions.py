class OrderError(Exception):
    """Base class for order-related exceptions."""
    status_code = 400

class OrderNotFoundError(OrderError):
    """Raised when an order is not found."""
    status_code = 404

class OrderInvalidStatusError(OrderError):
    """Raised when an order has an invalid status."""
    status_code = 422

class OrderStatusConflictError(OrderError):
    """Raised when there is a conflict in order status update."""
    status_code = 409