from fastapi import APIRouter, Depends, Query, HTTPException
from typing import Annotated
from src.schemas import (
    FilterPage,
    ResponsavelSchemaList,
    CriarResponsavelSchema,
)
from src.database import get_session
from sqlalchemy.orm import Session
from sqlalchemy import select
from src.models import Responsaveis
from http import HTTPStatus


router = APIRouter(prefix='/responsaveis', tags=['responsaveis'])

db_session = Annotated[Session, Depends(get_session)]


@router.get(
    '/', response_model=ResponsavelSchemaList, status_code=HTTPStatus.OK
)
async def get_alocacao(
    session: db_session, filter_users: Annotated[FilterPage, Query()]
):
    query = await session.scalars(
        select(Responsaveis)
        .offset(filter_users.offset)
        .limit(filter_users.limit)
    )
    responsaveis = query.all()
    if not responsaveis:
        raise HTTPException(
            status_code=404, detail='Nenhum responsavel encontrado'
        )
    return {'Responsaveis': responsaveis}


@router.post(
    '/', response_model=CriarResponsavelSchema, status_code=HTTPStatus.OK
)
async def post_alunos(
    new_responsavel: CriarResponsavelSchema, session: db_session
):
    aluno_repetido = await session.scalar(
        select(Responsaveis).where(
            Responsaveis.cpf == new_responsavel.cpf
            or Responsaveis.rg == new_responsavel.rg
        )
    )
    if aluno_repetido:
        raise HTTPException(status_code=400, detail='Cpf ou Rg já cadastrado')
    criar_responsavel = Responsaveis(**new_responsavel.model_dump())
    session.add(criar_responsavel)
    await session.commit()
    await session.refresh(criar_responsavel)

    return new_responsavel


@router.put('/')
def put_alunos():
    return {'hello': 'world'}


@router.delete('/')
def delete_alunos():
    return {'hello': 'world'}
