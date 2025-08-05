from fastapi import FastAPI
from injector import Injector
from fastapi_injector import attach_injector
from app.context.lifecycle import lifespan
from app.context.module import AppModule
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

    # TODO: add middleware
    # TODO: add api endpoint

    return app