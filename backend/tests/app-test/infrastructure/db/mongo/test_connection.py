import pytest
from unittest.mock import AsyncMock, Mock, patch
from app.infrastructure.db.mongo.connection import MongoDBConnection

@pytest.mark.asyncio
async def test_mongodb_connection_connect():
    mock_client = AsyncMock()
    mock_client.admin.command = AsyncMock(return_value={"ok": 1})
    mock_client.__getitem__.return_value = "mock_db"

    with patch("app.infrastructure.db.mongo.connection.AsyncIOMotorClient", return_value=mock_client):
        mongo = MongoDBConnection(uri="mongodb://localhost:27017", db_name="test_db")
        await mongo.connect()

        # Assert connection established
        mock_client.admin.command.assert_called_once_with("ping")
        assert mongo.client is mock_client
        assert mongo.db == "mock_db"

@pytest.mark.asyncio
async def test_mongodb_connection_disconnect():
    mock_client = Mock()
    mongo = MongoDBConnection(uri="mongodb://localhost:27017", db_name="test_db")
    mongo.client = mock_client

    await mongo.disconnect()

    mock_client.close.assert_called_once()
