class OrderDetailError(Exception):
    """Base exception for OrderDetail domain errors."""
    status_code = 400

class OrderDetailNotFoundError(OrderDetailError):
    """Raise when an order is not found."""
    status_code = 404

class InvalidOrderDetailDataError(OrderDetailError):
    """Raise when invalid order detail data is provided."""
    status_code = 422