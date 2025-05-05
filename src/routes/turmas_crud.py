from fastapi import APIRouter

router = APIRouter(prefix='/turmas', tags=['turmas'])


@router.get('/')
def hello():
    return {'hello': 'world'}
