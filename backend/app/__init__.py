from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware #+
from app.core.lifecycle import lifespan
from app.interfaces import api #+

def create_app() -> FastAPI:
    app = FastAPI(
        title="AI Short Video Generator",
        version="1.0.0",
        lifespan=lifespan
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_credentials=True,
        allow_headers=["*"],
    )

    app.include_router(api.router) #+

    return app

__all__ = ['create_app']