from fastapi import APIRouter, Depends, Query, HTTPException
from typing import Annotated
from src.schemas import FilterPage, CriarTurmaSchema, TurmaSchemaList
from src.database import get_session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from src.models import Turmas
from http import HTTPStatus


router = APIRouter(prefix='/turmas', tags=['turmas'])

db_session = Annotated[AsyncSession, Depends(get_session)]


@router.get('/', response_model=TurmaSchemaList, status_code=HTTPStatus.OK)
async def get_turmas(
    session: db_session, filter_users: Annotated[FilterPage, Query()]
):
    query = await session.scalars(
        select(Turmas).offset(filter_users.offset).limit(filter_users.limit)
    )
    turmas = query.all()
    if not turmas:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Nenhuma turma encontrada'
        )
    return {'Turmas': turmas}


@router.post(
    '/', response_model=CriarTurmaSchema, status_code=HTTPStatus.CREATED
)
async def post_turma(new_turma: CriarTurmaSchema, session: db_session):
    criar_turma = Turmas(**new_turma.model_dump())
    session.add(criar_turma)
    await session.commit()
    await session.refresh(criar_turma)

    return criar_turma


@router.put(
    '/{turma_id}', response_model=CriarTurmaSchema, status_code=HTTPStatus.OK
)
async def put_turma(
    turma_id: int, updated_turma: CriarTurmaSchema, session: db_session
):
    query = await session.scalars(
        select(Turmas).where(Turmas.id_turma == turma_id)
    )
    turma = query.first()

    if not turma:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Turma não encontrada'
        )

    turma.nome = updated_turma.nome
    turma.serie = updated_turma.serie
    turma.ano_letivo = updated_turma.ano_letivo
    turma.nivel = updated_turma.nivel
    turma.turno = updated_turma.turno
    turma.capacidade_maxima = updated_turma.capacidade_maxima
    turma.status = updated_turma.status

    await session.commit()
    await session.refresh(turma)
    return turma


@router.delete('/{turma_id}', status_code=HTTPStatus.OK)
async def delete_turma(turma_id: int, session: db_session):
    query = await session.scalars(
        select(Turmas).where(Turmas.id_turma == turma_id)
    )
    turma = query.first()
    if not turma:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Turma não encontrada'
        )
    await session.delete(turma)
    await session.commit()
    return {'detail': 'Turma deletada'}
