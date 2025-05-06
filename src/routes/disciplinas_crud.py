from fastapi import APIRouter

router = APIRouter(prefix='/disciplinas', tags=['disciplinas'])


@router.get('/')
def get_disciplinas():
    return {'hello': 'world'}
@router.post('/')
def post_disciplinas():
    return {'hello': 'world'}
@router.put('/')
def put_disciplinas():
    return {'hello': 'world'}
@router.delete('/')
def delete_disciplinas():
    return {'hello': 'world'}

