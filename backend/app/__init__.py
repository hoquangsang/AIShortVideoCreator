from fastapi import FastAPI
from app.core.lifecycle import lifespan

def create_app() -> FastAPI:
    app = FastAPI(
        title="AI Short Video Generator",
        version="1.0.0",
        lifespan=lifespan
    )

    return app

__all__ = ['create_app']