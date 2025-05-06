from fastapi import APIRouter

router = APIRouter(prefix='/professores', tags=['professores'])


@router.get('/')
def get_professores():
    return {'hello': 'world'}


@router.post('/')
def post_professores():
    return {'hello': 'world'}


@router.put('/')
def put_professores():
    return {'hello': 'world'}


@router.delete('/')
def delete_professores():
    return {'hello': 'world'}
