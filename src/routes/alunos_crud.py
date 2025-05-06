from fastapi import APIRouter

router = APIRouter(prefix='/alunos', tags=['alunos'])


@router.get('/')
def get_alunos():
    return {'hello': 'world'}
@router.post('/')
def post_alunos():
    return {'hello': 'world'}
@router.put('/')
def put_alunos():
    return {'hello': 'world'}
@router.delete('/')
def delete_alunos():
    return {'hello': 'world'}

