from injector import Module, Binder, singleton, provider
from app.core.infrastructure.db.mongo.client import MongoDBClient
from config.setting import settings


class AppModule(Module):
    def configure(self, binder: Binder):
        pass

    @singleton
    @provider
    def provide_mongodb_client(self) -> MongoDBClient:
        mongodb_client = MongoDBClient(
            uri=settings.MONGODB_URI,
            db_name=settings.MONGODB_DATABASE,
        )
        return mongodb_client
    
    # TODO