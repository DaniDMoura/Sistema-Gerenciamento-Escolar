from fastapi import APIRouter

router = APIRouter(prefix='/alocacoes', tags=['alocacoes'])


@router.get('/')
def hello():
    return {'hello': 'world'}
