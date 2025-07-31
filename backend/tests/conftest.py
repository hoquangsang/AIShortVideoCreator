import pytest
from fastapi import FastAPI
from httpx import AsyncClient
from httpx import ASGITransport

from app import create_app

@pytest.fixture
async def test_app() -> FastAPI:
    return create_app()

@pytest.fixture
async def async_client(test_app: FastAPI):
    transport = ASGITransport(app=test_app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        yield client