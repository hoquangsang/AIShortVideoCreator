from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.context.lifecycle import lifespan
from config.setting import settings


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.APP_NAME,
        version=settings.APP_VERSION,
        lifespan=lifespan
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ALLOW_ORIGINS_LIST,
        allow_methods=settings.CORS_ALLOW_METHODS_LIST,
        allow_headers=settings.CORS_ALLOW_HEADERS_LIST,
        allow_credentials=True,
    )

    return app