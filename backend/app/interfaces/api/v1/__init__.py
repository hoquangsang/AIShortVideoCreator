from fastapi import APIRouter

router = APIRouter(prefix='/v1')
@router.get('/ping')
async def ping():
    return {'message': 'pong'}

__all__ = ['router']