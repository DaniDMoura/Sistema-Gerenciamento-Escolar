from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routes import (
    alocacoes_crud,
    alunos_crud,
    disciplinas_crud,
    frequencias_crud,
    notas_crud,
    professores_crud,
    responsaveis_crud,
    turmas_crud,
)

origins = ['http://localhost:5173', 'http://localhost:8000']

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(alocacoes_crud.router, prefix='/api')
app.include_router(alunos_crud.router, prefix='/api')
app.include_router(disciplinas_crud.router, prefix='/api')
app.include_router(frequencias_crud.router, prefix='/api')
app.include_router(notas_crud.router, prefix='/api')
app.include_router(professores_crud.router, prefix='/api')
app.include_router(turmas_crud.router, prefix='/api')
app.include_router(responsaveis_crud.router, prefix='/api')
