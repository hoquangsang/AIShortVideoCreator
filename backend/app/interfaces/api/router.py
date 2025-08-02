from fastapi import APIRouter
router = APIRouter(prefix='/api')

from . import v1
router.include_router(v1.router)