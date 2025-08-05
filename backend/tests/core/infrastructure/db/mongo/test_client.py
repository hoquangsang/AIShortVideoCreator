import pytest
from unittest.mock import Mock, MagicMock, AsyncMock, patch
from app.core.infrastructure.db.mongo.client import MongoDBClient


# @pytest.mark.asynio
async def test_connect():
    # Setup init mock
    uri = 'mongodb://test:27017'
    db_name = 'test_db'

    # Setup mock method
    mock_async_motor_client = MagicMock()
    mock_async_motor_client.admin.command = AsyncMock(return_value={'ok':1})
    mock_async_motor_client.__getitem__.return_value = 'mock_db'

    # Replace AsyncIOMotorClient bymock_async_motor_client
    with patch('app.core.infrastructure.db.mongo.client.AsyncIOMotorClient', return_value=mock_async_motor_client):
        mongo = MongoDBClient(uri=uri, db_name=db_name)
        result = await mongo.connect()

        mock_async_motor_client.admin.command.assert_awaited_once_with('ping')
        assert result.database == 'mock_db'
        assert result.client is mock_async_motor_client


async def test_disconnect():
    # Setup init mock
    uri = 'mongodb://test:27017'
    db_name = 'test_db'

    # Setup mock
    mock_async_motor_client = MagicMock()

    #
    mongo = MongoDBClient(uri=uri, db_name=db_name)
    mongo.client = mock_async_motor_client

    #
    await mongo.disconnect()

    mock_async_motor_client.close.assert_called_once()