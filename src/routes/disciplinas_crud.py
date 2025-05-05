from fastapi import APIRouter

router = APIRouter(prefix='/disciplinas', tags=['disciplinas'])


@router.get('/')
def hello():
    return {'hello': 'world'}
