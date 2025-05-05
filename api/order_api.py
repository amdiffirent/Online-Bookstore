from fastapi import APIRouter, HTTPException
from typing import List
from models.order import Order
from services.order_service import OrderService
from repositories.order_repository import OrderRepository
from repositories.user_repository import UserRepository
from repositories.book_repository import BookRepository

router = APIRouter(prefix="/api/orders", tags=["Orders"])

order_service = OrderService(
    OrderRepository(),
    UserRepository(),
    BookRepository()
)

@router.post("/", response_model=Order)
def place_order(order: Order):
    try:
        return order_service.place_order(order)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/user/{user_id}", response_model=List[Order])
def get_orders_by_user(user_id: str):
    try:
        return order_service.get_orders_by_user(user_id)
    except ValueError:
        raise HTTPException(status_code=404, detail="User not found")
