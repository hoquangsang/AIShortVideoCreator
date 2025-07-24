import pytest
from unittest.mock import AsyncMock, patch
from app.core.container import AppContainer

@pytest.mark.asyncio
async def test_appcontainer_startup_shutdown():
    container = AppContainer()
    container.mongo_conn = AsyncMock()
    
    # mock connect & disconnect
    container.mongo_conn.connect = AsyncMock()
    container.mongo_conn.disconnect = AsyncMock()
    
    await container.startup()
    container.mongo_conn.connect.assert_awaited_once()
    
    await container.shutdown()
    container.mongo_conn.disconnect.assert_awaited_once()
