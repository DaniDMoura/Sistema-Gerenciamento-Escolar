from fastapi import APIRouter

router = APIRouter(prefix='/alocacoes', tags=['alocacoes'])


@router.get('/')
def get_alocacao():
    return {'hello': 'world'}
@router.post('/')
def post_alocacao():
    return {'hello': 'world'}
@router.put('/')
def put_alocacao():
    return {'hello': 'world'}
@router.delete('/')
def delete_alocacao():
    return {'hello': 'world'}

