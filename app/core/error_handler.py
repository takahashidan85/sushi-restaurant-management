from .responses import error_response
from marshmallow import ValidationError

from app.modules.customer.domain.exceptions import CustomerError
from app.modules.sushi_item.domain.exceptions import SushiItemError
from app.modules.order.domain.exceptions import OrderError
from app.modules.order_detail.domain.exceptions import OrderDetailError

def register_error_handlers(app):
    """Register error handlers for the Flask app."""
    @app.errorhandler(ValidationError)
    def handle_validation_error(err):
        return error_response("Validation Error", 400, err.messages)

    @app.errorhandler(Exception)
    def handle_generic_error(err):
        return error_response("Internal Server Error", 500)

    
    @app.errorhandler(CustomerError)
    @app.errorhandler(SushiItemError)
    @app.errorhandler(OrderError)
    @app.errorhandler(OrderDetailError)
    def handle_domain_error(err):
        return error_response(str(err), getattr(err, "status_code", 400))
