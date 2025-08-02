import pytest
from unittest.mock import AsyncMock, patch, MagicMock
from app.infrastructure.db.mongo.client import MongoDBClient


@pytest.mark.asyncio
async def test_mongodb_client_enter():
    mock_motor_client = AsyncMock()
    mock_motor_client.admin.command = AsyncMock(return_value={"ok": 1})
    mock_motor_client.__getitem__.return_value = "mock_db"

    with patch("app.infrastructure.db.mongo.client.AsyncIOMotorClient", return_value=mock_motor_client):
        mongo = MongoDBClient(uri="mongodb://localhost:27017", db_name="test_db")
        async with mongo as client:
            # Assert
            mock_motor_client.admin.command.assert_called_once_with("ping")
            assert client.client is mock_motor_client
            assert client.database == "mock_db"


@pytest.mark.asyncio
async def test_mongodb_client_exit():
    mock_motor_client = AsyncMock()
    mongo = MongoDBClient(uri="mongodb://localhost:27017", db_name="test_db")
    mongo.client = mock_motor_client

    await mongo.__aexit__(None, None, None)

    mock_motor_client.close.assert_called_once()
