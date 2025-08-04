import pytest
from httpx import AsyncClient

# @pytest.mark.asyncio
async def test_app_starts(async_client: AsyncClient):
    response = await async_client.get("/")
    assert response.status_code in [200, 404]  # Do chưa có route nào