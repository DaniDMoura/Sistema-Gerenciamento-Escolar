from fastapi import APIRouter, Depends, Query, HTTPException
from typing import Annotated
from src.schemas import FilterPage, DisciplinaSchemaList, CriarDisciplinaSchema
from src.database import get_session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from src.models import Disciplinas
from http import HTTPStatus


router = APIRouter(prefix='/disciplinas', tags=['disciplinas'])

db_session = Annotated[AsyncSession, Depends(get_session)]


@router.get(
    '/', response_model=DisciplinaSchemaList, status_code=HTTPStatus.OK
)
async def get_disciplinas(
    session: db_session, filter_users: Annotated[FilterPage, Query()]
):
    query = await session.scalars(
        select(Disciplinas)
        .offset(filter_users.offset)
        .limit(filter_users.limit)
    )
    disciplinas = query.all()
    if not disciplinas:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Nenhuma disciplina encontrada',
        )
    return {'Disciplinas': disciplinas}


@router.post(
    '/', response_model=CriarDisciplinaSchema, status_code=HTTPStatus.CREATED
)
async def post_disciplinas(
    new_disciplina: CriarDisciplinaSchema, session: db_session
):
    criar_disciplina = Disciplinas(**new_disciplina.model_dump())
    session.add(criar_disciplina)
    await session.commit()
    await session.refresh(criar_disciplina)

    return criar_disciplina


@router.put(
    '/{disciplina_id}',
    response_model=CriarDisciplinaSchema,
    status_code=HTTPStatus.OK,
)
async def put_disciplinas(
    disciplina_id: int,
    updated_disciplina: CriarDisciplinaSchema,
    session: db_session,
):
    result = await session.scalars(
        select(Disciplinas).where(Disciplinas.id_disciplina == disciplina_id)
    )
    disciplina = result.first()

    if not disciplina:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Disciplina não encontrada',
        )

    disciplina.nome = updated_disciplina.nome
    disciplina.descricao = updated_disciplina.descricao
    disciplina.carga_horaria = updated_disciplina.carga_horaria
    disciplina.nivel = updated_disciplina.nivel
    disciplina.area_conhecimento = updated_disciplina.area_conhecimento
    disciplina.obrigatoria = updated_disciplina.obrigatoria

    await session.commit()
    await session.refresh(disciplina)
    return disciplina


@router.delete('/{disciplina_id}', status_code=HTTPStatus.OK)
async def delete_disciplinas(disciplina_id: int, session: db_session):
    disciplina = await session.scalar(
        select(Disciplinas).where(Disciplinas.id_disciplina == disciplina_id)
    )
    if not disciplina:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Disciplina não encontrada',
        )
    await session.delete(disciplina)
    await session.commit()
    return {'detail': 'Disciplina deletada'}
