from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.dependencies.container import Container

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        container = Container()
        app.state.container = container  # attach to app if needed

        # TODO: init resouces
        container.wire()

        yield
    finally: 
        # TODO: shutdown resouces
        container.unwire()
