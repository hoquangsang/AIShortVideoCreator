from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.core.container import AppContainer

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.container = AppContainer()
    try:
        await app.state.container.startup()
        yield
    finally:
        await app.state.container.shutdown()
