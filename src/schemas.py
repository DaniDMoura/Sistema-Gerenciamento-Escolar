from pydantic import BaseModel, EmailStr
from datetime import date, datetime
from typing import Optional
from enum import Enum


class StatusEnum(str, Enum):
    ativo = 'ativo'
    inativo = 'inativo'
    concluido = 'concluido'
    pendente = 'pendente'
    expulso = 'expulso'
    falecido = 'falecido'
    transferido = 'transferido'


class SexoEnum(str, Enum):
    masculino = 'masculino'
    feminino = 'feminino'
    outro = 'outro'


class AlunoSchema(BaseModel):
    id_aluno: int
    nome: str
    sobrenome: str
    data_nascimento: date
    sexo: SexoEnum
    cpf: str
    rg: str
    endereco: str
    cep: str
    email: EmailStr
    telefone: str
    status: Optional[StatusEnum] = StatusEnum.ativo
    foto: Optional[str]
    necessidades: Optional[str]
    grupo_sanguineo: Optional[str]
    medicamentos: Optional[str]
    id_responsavel: Optional[int]

    class Config:
        from_attributes = True


class AlunoSchemaList(BaseModel):
    Alunos: list[AlunoSchema]


class CriarAlunosSchema(BaseModel):
    nome: str
    sobrenome: str
    data_nascimento: date
    sexo: SexoEnum
    cpf: str
    rg: str
    endereco: str
    cep: str
    email: EmailStr
    telefone: str
    status: Optional[StatusEnum] = StatusEnum.ativo
    foto: Optional[str] = 'https://placehold.co/200x200'
    necessidades: Optional[str] = 'Não especificado'
    grupo_sanguineo: Optional[str] = 'Não especificado'
    medicamentos: Optional[str] = 'Nenhum medicamento'
    id_responsavel: Optional[int]

    class Config:
        from_attributes = True


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
        from_attributes = True


class CriarResponsavelSchema(BaseModel):
    nome: str
    sobrenome: str
    parentesco: Optional[str]
    cpf: str
    rg: str
    endereco: str
    cep: str
    email: str
    telefone: str
    autorizado_buscar: bool

    class Config:
        from_attributes = True


class ResponsavelSchemaList(BaseModel):
    Responsaveis: list[ResponsavelSchema]


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
        from_attributes = True


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
        from_attributes = True


class DisciplinaSchema(BaseModel):
    id_disciplina: int
    nome: str
    descricao: str
    carga_horaria: int
    area_conhecimento: str
    obrigatoria: bool

    class Config:
        from_attributes = True


class AlocacaoSchema(BaseModel):
    id_alocacao: int
    id_professor: int
    id_disciplina: int
    id_turma: int

    class Config:
        from_attributes = True


class NotaSchema(BaseModel):
    id_nota: int
    id_aluno: int
    id_disciplina: int
    bimestre: int
    valor: float
    data_lancamento: datetime

    class Config:
        from_attributes = True


class FrequenciaSchema(BaseModel):
    id_frequencia: int
    id_aluno: int
    id_disciplina: int
    data: date
    presente: bool

    class Config:
        from_attributes = True


class FilterPage(BaseModel):
    offset: int = 0
    limit: int = 100
