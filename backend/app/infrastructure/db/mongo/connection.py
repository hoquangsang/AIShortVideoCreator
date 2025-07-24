from motor.motor_asyncio import AsyncIOMotorClient


class MongoDBConnection:
    def __init__(self, uri: str, db_name: str):
        """
        :param uri: MongoDB connection URI
        :param db_name: Database name to use
        """
        self.uri = uri
        self.db_name = db_name
        self.client: AsyncIOMotorClient | None = None
        self.db = None

    async def connect(self):
        """
        Connect to MongoDB and select the database.
        """
        self.client = AsyncIOMotorClient(self.uri)
        await self.client.admin.command("ping")
        self.db = self.client[self.db_name]

    async def disconnect(self):
        """
        Close the MongoDB connection.
        """
        if self.client:
            self.client.close()
