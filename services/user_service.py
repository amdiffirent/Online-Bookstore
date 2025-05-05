from typing import List
from models.user import User
from repositories.user_repository import UserRepository

class UserService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def create_user(self, user: User) -> User:
        self.user_repo.save(user)
        return user

    def get_user(self, user_id: str) -> User:
        user = self.user_repo.find_by_id(user_id)
        if not user:
            raise ValueError(f"User with ID '{user_id}' not found")
        return user

    def get_all_users(self) -> List[User]:
        return self.user_repo.find_all()

