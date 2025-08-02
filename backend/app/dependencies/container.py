from dependency_injector import containers, providers
from app.infrastructure.db.mongo.client import MongoDBClient


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    mongodb_client = providers.Resource(
        MongoDBClient,
        uri=config.mongodb_client.uri,
        db_name=config.mongodb_client.db_name,
    )
    # TODO:
    