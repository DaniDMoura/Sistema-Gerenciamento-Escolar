from fastapi import APIRouter

router = APIRouter(prefix='/frequencias', tags=['frequencias'])


@router.get('/')
def get_frequencias():
    return {'hello': 'world'}


@router.post('/')
def post_frequencias():
    return {'hello': 'world'}


@router.put('/')
def put_frequencias():
    return {'hello': 'world'}


@router.delete('/')
def delete_frequencias():
    return {'hello': 'world'}
