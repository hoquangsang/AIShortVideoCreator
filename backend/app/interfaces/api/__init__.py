from . import v1
from fastapi import APIRouter

router = APIRouter(prefix='/api')
router.include_router(v1.router)

__all__ = ['router']