from fastapi import APIRouter

router = APIRouter(prefix='/professores', tags=['professores'])


@router.get('/')
def hello():
    return {'hello': 'world'}
