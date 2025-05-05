from fastapi import APIRouter

router = APIRouter(prefix='/frequencias', tags=['frequencias'])


@router.get('/')
def hello():
    return {'hello': 'world'}
