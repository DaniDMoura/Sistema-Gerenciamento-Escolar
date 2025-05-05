from fastapi import APIRouter

router = APIRouter(prefix='/notas', tags=['notas'])


@router.get('/')
def hello():
    return {'hello': 'world'}
