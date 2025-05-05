from pydantic import BaseModel, EmailStr
from datetime import date, datetime
from typing import Optional


class AlunoSchema(BaseModel):
    id_aluno: int
    nome: str
    sobrenome: str
    data_nascimento: date
    sexo: str
    cpf: str
    rg: str
    endereco: str
    cep: str
    email: EmailStr
    telefone: str
    foto: Optional[str]
    status: str
    necessidades: Optional[str]
    grupo_sanguineo: Optional[str]
    medicamentos: Optional[str]
    id_responsavel: Optional[int]

    class Config:
        orm_mode = True


class ResponsavelSchema(BaseModel):
    id_responsavel: int
    nome: str
    sobrenome: str
    parentesco: Optional[str]
    cpf: str
    rg: str
    endereco: str
    email: str
    telefone: str
    autorizado_buscar: bool

    class Config:
        orm_mode = True


class ProfessorSchema(BaseModel):
    id_professor: int
    nome: str
    sobrenome: str
    data_nascimento: date
    sexo: str
    cpf: str
    rg: str
    endereco: str
    telefone: str
    email: EmailStr
    data_admissao: date
    formacao_academica: str
    area_especializacao: str
    carga_horaria_semanal: int
    status: str
    foto: Optional[str]

    class Config:
        orm_mode = True


class TurmaSchema(BaseModel):
    id_turma: int
    ano_letivo: int
    nome: str
    serie: str
    nivel: str
    turno: str
    capacidade_maxima: Optional[int]
    status: str

    class Config:
        orm_mode = True


class DisciplinaSchema(BaseModel):
    id_disciplina: int
    nome: str
    descricao: str
    carga_horaria: int
    area_conhecimento: str
    obrigatoria: bool

    class Config:
        orm_mode = True


class AlocacaoSchema(BaseModel):
    id_alocacao: int
    id_professor: int
    id_disciplina: int
    id_turma: int

    class Config:
        orm_mode = True


class NotaSchema(BaseModel):
    id_nota: int
    id_aluno: int
    id_disciplina: int
    bimestre: int
    valor: float
    data_lancamento: datetime

    class Config:
        orm_mode = True


class FrequenciaSchema(BaseModel):
    id_frequencia: int
    id_aluno: int
    id_disciplina: int
    data: date
    presente: bool

    class Config:
        orm_mode = True
