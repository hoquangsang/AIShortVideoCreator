from fastapi import FastAPI

def create_app() -> FastAPI:
    app = FastAPI(title="AI Short Video Creator")
    return app

__all__ = ['create_app']