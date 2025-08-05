import pytest
from httpx import AsyncClient



async def test_ping(async_client: AsyncClient):
    response = await async_client.get('/api/v1/ping')
    assert response.status_code == 200
    assert response.json() == {'message': 'pong'}