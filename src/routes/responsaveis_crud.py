from fastapi import APIRouter

router = APIRouter(prefix='/responsaveis', tags=['responsaveis'])


@router.get('/')
def get_responsaveis():
    return {'hello': 'world'}
@router.post('/')
def post_responsaveis():
    return {'hello': 'world'}
@router.put('/')
def put_responsaveis():
    return {'hello': 'world'}
@router.delete('/')
def delete_responsaveis():
    return {'hello': 'world'}

