from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase


class MongoDBClient:
    def __init__(self, uri: str, db_name: str):
        """
        :param uri: MongoDB connection URI
        :param db_name: Database name to use
        """
        self.uri = uri
        self.db_name = db_name
        self.database: AsyncIOMotorDatabase|None = None
        self.client: AsyncIOMotorClient|None = None
    
    async def connect(self):
        """
        Connect to mongo and select database
        """
        self.client = AsyncIOMotorClient(self.uri)
        await self.client.admin.command('ping')
        self.database = self.client[self.db_name]
        return self

    async def disconnect(self):
        """
        Disconnect to mongo
        """
        if self.client:
            self.client.close()