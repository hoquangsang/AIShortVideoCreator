from fastapi import FastAPI
from config.setting import settings
from app.context.lifecycle import lifespan


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.APP_NAME,
        version=settings.APP_VERSION,
        lifespan=lifespan
    )

    return app