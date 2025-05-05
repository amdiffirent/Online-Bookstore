from models.order import Order
from repositories.order_repository import OrderRepository
from repositories.user_repository import UserRepository
from repositories.book_repository import BookRepository

class OrderService:
    def __init__(self, order_repo: OrderRepository, user_repo: UserRepository, book_repo: BookRepository):
        self.order_repo = order_repo
        self.user_repo = user_repo
        self.book_repo = book_repo

    def place_order(self, order: Order) -> Order:
        user = self.user_repo.find_by_id(order.user_id)
        if not user:
            raise ValueError("User not found")

        existing_orders = self.order_repo.find_by_user_id(order.user_id)
        if len(existing_orders) >= 5:
            raise ValueError("User cannot place more than 5 orders")

        for book_id in order.book_ids:
            book = self.book_repo.find_by_id(book_id)
            if not book:
                raise ValueError(f"Book ID {book_id} not found")

        self.order_repo.save(order)
        return order

