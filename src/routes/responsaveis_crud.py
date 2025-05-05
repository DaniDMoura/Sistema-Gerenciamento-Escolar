from fastapi import APIRouter

router = APIRouter(prefix='/responsaveis', tags=['responsaveis'])


@router.get('/')
def hello():
    return {'hello': 'world'}
