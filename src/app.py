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

origins = [
    "http://localhost:5173",
]

app = FastAPI()

app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

app.include_router(alocacoes_crud.router, prefix='/alocacoes')
app.include_router(alunos_crud.router, prefix='/alunos')
app.include_router(disciplinas_crud.router, prefix='/disciplinas')
app.include_router(frequencias_crud.router, prefix='/frequencias')
app.include_router(notas_crud.router, prefix='/notas')
app.include_router(professores_crud.router, prefix='/professores')
app.include_router(turmas_crud.router, prefix='/turmas')
app.include_router(responsaveis_crud.router, prefix='/responsaveis')
