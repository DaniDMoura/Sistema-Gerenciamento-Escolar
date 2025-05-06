from fastapi import APIRouter

router = APIRouter(prefix='/turmas', tags=['turmas'])


@router.get('/')
def get_turmas():
    return {'hello': 'world'}
@router.post('/')
def post_turmas():
    return {'hello': 'world'}
@router.put('/')
def put_turmas():
    return {'hello': 'world'}
@router.delete('/')
def delete_turmas():
    return {'hello': 'world'}

