
import pytest
from online_bookstore.services.user_service import UserService
from online_bookstore.models.user import User

class MockUserRepository:
    def __init__(self):
        self.users = {}

    def save(self, user):
        self.users[user.id] = user
        return user

    def find_by_id(self, user_id):
        return self.users.get(user_id)

    def find_all(self):
        return list(self.users.values())

@pytest.fixture
def user_repo():
    return MockUserRepository()

@pytest.fixture
def user_service(user_repo):
    return UserService(user_repo)

def test_create_user(user_service):
    user = User(id="u1", name="Alice")
    created = user_service.create_user(user)
    assert created.name == "Alice"

def test_get_user_valid(user_service):
    user = User(id="u1", name="Bob")
    user_service.create_user(user)
    found = user_service.get_user("u1")
    assert found.id == "u1"

def test_get_user_invalid(user_service):
    with pytest.raises(ValueError):
        user_service.get_user("ghost")
