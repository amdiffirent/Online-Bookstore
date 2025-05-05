import pytest
from httpx import AsyncClient
from main import app

@pytest.mark.asyncio
async def test_create_and_get_book():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        # Create book
        response = await ac.post("/api/books/", json={
            "id": "b001",
            "title": "Test Book",
            "author": "Tester",
            "price": 120.0,
            "in_stock": True
        })
        assert response.status_code == 200

        # Get all books
        response = await ac.get("/api/books/")
        assert response.status_code == 200
        assert isinstance(response.json(), list)

