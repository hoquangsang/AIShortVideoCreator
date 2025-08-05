from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from injector import Injector
from fastapi_injector import attach_injector
from app.context.lifecycle import lifespan
from app.context.module import AppModule
from app.core.interfaces.http.api import router as api_router
from config.setting import settings


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.APP_NAME,
        version=settings.APP_VERSION,
        lifespan=lifespan,
    )

    #
    injector = Injector([AppModule()])
    app.state.injector = injector
    attach_injector(
        app=app,
        injector=injector
    )

    # add middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ALLOW_ORIGINS_LIST,
        allow_methods=settings.CORS_ALLOW_METHODS_LIST,
        allow_headers=settings.CORS_ALLOW_HEADERS_LIST,
        allow_credentials=settings.CORS_ALLOW_CREDENTIALS,
    )

    # add router
    app.include_router(api_router)

    return app