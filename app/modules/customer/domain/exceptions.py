class CustomerError(Exception):
    """Base class for customer-related exceptions."""
    status_code = 400

class CustomerNotFoundError(CustomerError):
    """Raised when a customer is not found."""
    status_code = 404

class CustomerAlreadyExistsError(CustomerError):
    """Raised when attempting to create a customer that already exists."""
    status_code = 409
    