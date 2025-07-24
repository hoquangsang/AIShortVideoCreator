from config import app_settings
from app.infrastructure.db import MongoDBConnection
import logging

logger = logging.getLogger('uvicorn')

class AppContainer:
    def __init__(self):
        self.mongo_conn = MongoDBConnection(
            uri=app_settings.MONGODB_URI,
            db_name=app_settings.MONGODB_NAME
        )
        
    async def startup(self):
        await self.mongo_conn.connect()
        logger.info("MongoDB connected and ready")

    async def shutdown(self):
        if self.mongo_conn:
            await self.mongo_conn.disconnect()
            logger.info("MongoDB disconnected")