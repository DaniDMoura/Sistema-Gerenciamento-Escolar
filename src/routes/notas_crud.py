from fastapi import APIRouter

router = APIRouter(prefix='/notas', tags=['notas'])


@router.get('/')
def get_notas():
    return {'hello': 'world'}
@router.post('/')
def post_notas():
    return {'hello': 'world'}
@router.put('/')
def put_notas():
    return {'hello': 'world'}
@router.delete('/')
def delete_notas():
    return {'hello': 'world'}

