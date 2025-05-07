from fastapi import APIRouter, Depends
from typing import Annotated
from src.database import get_session
from sqlalchemy.orm import Session


router = APIRouter(prefix='/alocacoes', tags=['alocacoes'])

db_session = Annotated[Session, Depends(get_session)]


@router.get('/')
def get_alocacao(session: db_session):
    return {'hello': 'world'}


@router.post('/')
def post_alocacao(session: db_session):
    return {'hello': 'world'}


@router.put('/')
def put_alocacao(session: db_session):
    return {'hello': 'world'}


@router.delete('/')
def delete_alocacao(session: db_session):
    return {'hello': 'world'}
