class SushiItemError(Exception):
    """Base exception for SushiItem domain errors."""
    status_code = 400

class SushiItemNotFoundError(SushiItemError):
    """Exception raised when an item is not found."""
    status_code = 404

class SushiItemAlreadyExistsError(SushiItemError):
    """Exception raised when an item name already exists."""
    status_code = 409

class InvalidSushiItemDataError(SushiItemError):
    """Exception raised when an invalid item data is provided."""
    status_code = 422