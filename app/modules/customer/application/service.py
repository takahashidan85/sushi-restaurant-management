from ..infrastructure.repository import CustomerRepository

class CustomerService:
    """Service layer for Customer operations."""

    @staticmethod
    def create(name: str, email: str):
        return CustomerRepository.add(name, email)
    
    @staticmethod
    def list_all():
        return CustomerRepository.list_all()
    
    @staticmethod
    def get(customer_id: int):
        return CustomerRepository.get(customer_id)
    
    @staticmethod
    def update(customer_id: int, name: str | None, email: str | None):
        return CustomerRepository.update(customer_id, name, email)
    
    @staticmethod
    def delete(customer_id: int):
        return CustomerRepository.delete(customer_id)