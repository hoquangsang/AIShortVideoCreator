from contextlib import asynccontextmanager
from fastapi import FastAPI
from injector import Injector
from config.logging import logger
from app.core.infrastructure.db.mongo.client import MongoDBClient


@asynccontextmanager
async def lifespan(app: FastAPI):
    injector: Injector = app.state.injector

    # TODO: startup
    mongo = injector.get(MongoDBClient)
    await mongo.connect()
    logger.info("🚀 MongoDB connected successfully!")
    
    yield

    # TODO: shutdown
    await mongo.disconnect()
    logger.info("🧹 MongoDB disconnected successfully!")