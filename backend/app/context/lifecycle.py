import traceback, sys
from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.dependencies.container import Container
from config.setting import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        container = Container()
        app.state.container = container  # attach to app if needed

        container.config.from_dict({
            'mongodb_client': {
                'uri': settings.MONGODB_URI,
                'db_name': settings.MONGODB_DATABASE,
            },
        }, required=True)        
        await container.init_resources()
        container.wire(packages=['app.interfaces.api'])

        yield
    except Exception:
        traceback.print_exc()
        sys.exit(1)
    finally:
        try:
            await container.shutdown_resources()
        except Exception:
            traceback.print_exc()
        container.unwire()
