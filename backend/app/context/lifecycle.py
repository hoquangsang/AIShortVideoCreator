from contextlib import asynccontextmanager
from fastapi import FastAPI
from injector import Injector
from config.logging import logger


@asynccontextmanager
async def lifespan(app: FastAPI):
    injector: Injector = app.state.injector

    # TODO: startup
    logger.info("🚀 Startup...")
    
    yield

    # TODO: shutdown
    logger.info("🧹 Shutdown...")