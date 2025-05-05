import pytest
from httpx import AsyncClient
from main import app

@pytest.mark.asyncio
async def test_create_and_get_user():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        # Create user
        response = await ac.post("/api/users/", json={
            "id": "u001",
            "name": "Test User",
            "email": "user@example.com"
        })
        assert response.status_code == 200

        # Get all users
        response = await ac.get("/api/users/")
        assert response.status_code == 200
        assert isinstance(response.json(), list)
