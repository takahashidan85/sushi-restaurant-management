from app.infrastructure.repositories.order_repo import OrderRepository

class OrderService:
    @staticmethod
    def create(customer_id: int):
        return OrderRepository.add(customer_id)

    @staticmethod
    def list_all():
        return OrderRepository.list_all()

    @staticmethod
    def get(order_id: int):
        return OrderRepository.get(order_id)
    
    @staticmethod
    def update(order_id, customer_id=None):
        return OrderRepository.update(order_id, customer_id)    

    @staticmethod
    def delete(order_id: int) -> bool:
        return OrderRepository.delete(order_id)
