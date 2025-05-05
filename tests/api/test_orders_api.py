import pytest
from httpx import AsyncClient
from main import app

@pytest.mark.asyncio
async def test_place_order():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        # Create user and book first
        await ac.post("/api/users/", json={
            "id": "u002", "name": "Buyer", "email": "buyer@test.com"
        })
        await ac.post("/api/books/", json={
            "id": "b002", "title": "Buyable Book", "author": "Author B", "price": 99.99, "in_stock": True
        })

        # Place order
        response = await ac.post("/api/orders/", json={
            "id": "o001",
            "user_id": "u002",
            "book_ids": ["b002"]
        })
        assert response.status_code == 200
        assert response.json()["id"] == "o001"
