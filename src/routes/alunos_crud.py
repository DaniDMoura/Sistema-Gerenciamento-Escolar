from fastapi import APIRouter

router = APIRouter(prefix='/alunos', tags=['alunos'])


@router.get('/')
def hello():
    return {'hello': 'world'}
