
from fastapi import APIRouter, HTTPException
from typing import List
from models.user import User
from services.user_service import UserService
from repositories.user_repository import UserRepository

router = APIRouter(prefix="/api/users", tags=["Users"])

user_service = UserService(UserRepository())

@router.post("/", response_model=User)
def create_user(user: User):
    return user_service.create_user(user)

@router.get("/", response_model=List[User])
def get_all_users():
    return user_service.get_all_users()

@router.get("/{user_id}", response_model=User)
def get_user(user_id: str):
    try:
        return user_service.get_user(user_id)
    except ValueError:
        raise HTTPException(status_code=404, detail="User not found")
