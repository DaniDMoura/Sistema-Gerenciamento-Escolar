from fastapi import APIRouter, Depends, Query, HTTPException
from typing import Annotated
from src.schemas import FilterPage, AlunoSchemaList, CriarAlunosSchema
from src.database import get_session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from src.models import Alunos
from http import HTTPStatus


router = APIRouter(prefix='/alunos', tags=['alunos'])

db_session = Annotated[AsyncSession, Depends(get_session)]


@router.get('/', response_model=AlunoSchemaList, status_code=HTTPStatus.OK)
async def get_alunos(
    session: db_session, filter_users: Annotated[FilterPage, Query()]
):
    query = await session.scalars(
        select(Alunos).offset(filter_users.offset).limit(filter_users.limit)
    )
    alunos = query.all()
    if not alunos:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Nenhum aluno encontrado'
        )
    return {'Alunos': alunos}


@router.post(
    '/', response_model=CriarAlunosSchema, status_code=HTTPStatus.CREATED
)
async def post_alunos(new_aluno: CriarAlunosSchema, session: db_session):
    aluno_repetido = await session.scalar(
        select(Alunos).where(
            (Alunos.cpf == new_aluno.cpf) | (Alunos.rg == new_aluno.rg)
        )
    )
    if aluno_repetido:
        raise HTTPException(
            status_code=HTTPStatus.CONFLICT, detail='Cpf ou Rg já cadastrado'
        )
    criar_aluno = Alunos(**new_aluno.model_dump())
    session.add(criar_aluno)
    await session.commit()
    await session.refresh(criar_aluno)

    return new_aluno


@router.put(
    '/{aluno_id}', response_model=CriarAlunosSchema, status_code=HTTPStatus.OK
)
async def put_alunos(
    aluno_id: int, updated_aluno: CriarAlunosSchema, session: db_session
):
    result = await session.scalars(
        select(Alunos).where(Alunos.id_aluno == aluno_id)
    )
    aluno = result.first()

    if not aluno:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Aluno não encontrado'
        )

    aluno_repetido = await session.scalars(
        select(Alunos).where(
            (
                (Alunos.cpf == updated_aluno.cpf)
                | (Alunos.rg == updated_aluno.rg)
            )
            & (Alunos.id_aluno != aluno_id)
        )
    )
    if aluno_repetido.first():
        raise HTTPException(
            status_code=HTTPStatus.CONFLICT, detail='Cpf ou Rg já cadastrado'
        )

    aluno.nome = updated_aluno.nome
    aluno.sobrenome = updated_aluno.sobrenome
    aluno.data_nascimento = updated_aluno.data_nascimento
    aluno.sexo = updated_aluno.sexo
    aluno.cpf = updated_aluno.cpf
    aluno.rg = updated_aluno.rg
    aluno.endereco = updated_aluno.endereco
    aluno.cep = updated_aluno.cep
    aluno.email = updated_aluno.email
    aluno.telefone = updated_aluno.telefone
    aluno.foto = updated_aluno.foto
    aluno.status = updated_aluno.status
    aluno.necessidades = updated_aluno.necessidades
    aluno.grupo_sanguineo = updated_aluno.grupo_sanguineo
    aluno.medicamentos = updated_aluno.medicamentos

    await session.commit()
    await session.refresh(aluno)
    return aluno


@router.delete('/{user_id}', status_code=HTTPStatus.OK)
async def delete_alunos(aluno_id: int, session: db_session):
    query = await session.scalar(
        select(Alunos).where(Alunos.id_aluno == aluno_id)
    )
    aluno = query
    if not aluno:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Aluno não encontrado'
        )
    await session.delete(aluno)
    await session.commit()
    return {'detail': 'Aluno deletado'}
