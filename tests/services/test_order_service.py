
import pytest
from online_bookstore.services.order_service import OrderService
from online_bookstore.models.order import Order
from online_bookstore.models.user import User
from online_bookstore.models.book import Book

class MockRepo:
    def __init__(self):
        self.store = {}

    def save(self, entity):
        self.store[entity.id] = entity
        return entity

    def find_by_id(self, entity_id):
        return self.store.get(entity_id)

    def find_by_user_id(self, user_id):
        return [order for order in self.store.values() if order.user_id == user_id]

@pytest.fixture
def user_repo():
    repo = MockRepo()
    user = User(id="u1", name="Alice")
    repo.save(user)
    return repo

@pytest.fixture
def book_repo():
    repo = MockRepo()
    repo.save(Book(id="b1", title="Book 1", author="X", price=10))
    repo.save(Book(id="b2", title="Book 2", author="Y", price=12))
    return repo

@pytest.fixture
def order_repo():
    return MockRepo()

@pytest.fixture
def order_service(order_repo, user_repo, book_repo):
    return OrderService(order_repo, user_repo, book_repo)

def test_place_order_success(order_service):
    order = Order(id="o1", user_id="u1", book_ids=["b1", "b2"])
    placed = order_service.place_order(order)
    assert placed.id == "o1"

def test_place_order_user_not_found(order_service):
    order = Order(id="o2", user_id="ghost", book_ids=["b1"])
    with pytest.raises(ValueError, match="User not found"):
        order_service.place_order(order)

def test_place_order_too_many(order_service):
    for i in range(5):
        order = Order(id=f"o{i}", user_id="u1", book_ids=["b1"])
        order_service.place_order(order)
    with pytest.raises(ValueError, match="more than 5"):
        order_service.place_order(Order(id="o6", user_id="u1", book_ids=["b2"]))

def test_place_order_invalid_book(order_service):
    order = Order(id="o3", user_id="u1", book_ids=["invalid"])
    with pytest.raises(ValueError, match="Book ID invalid not found"):
        order_service.place_order(order)
