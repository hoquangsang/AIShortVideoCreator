from fastapi import APIRouter


router = APIRouter(prefix='/v1')

@router.get(path='/ping')
def get_ping():
    return {'message': 'pong'}

# TODO: include_router(<feat>)