from sqlalchemy.orm import Mapped, mapped_column, registry, relationship
from datetime import date
from sqlalchemy import ForeignKey, func

table_registry = registry()

@table_registry.mapped_as_dataclass
class Aluno:
  __tablename__ = "Aluno"

  id_aluno: Mapped[int] = mapped_column(init=False, primary_key=True)
  nome: Mapped[str]
  sobrenome: Mapped[str]
  data_nascimento: Mapped[date]
  sexo: Mapped[str]
  cpf: Mapped[str]
  rg: Mapped[str]
  endereco: Mapped[str]
  cep: Mapped[str]
  email: Mapped[str]
  telefone: Mapped[str]
  foto: Mapped[str] = mapped_column(nullable=True)
  status: Mapped[str]
  necessidades: Mapped[str] = mapped_column(nullable=True)
  grupo_sanguineo: Mapped[str] = mapped_column(nullable=True)
  medicamentos: Mapped[str] = mapped_column(nullable=True)

  id_responsavel: Mapped[int] = mapped_column(ForeignKey("Responsaveis.id_responsavel"))
  responsavel: Mapped["Responsaveis"] = relationship(init=False, back_populates="alunos")

@table_registry.mapped_as_dataclass
class Responsaveis:
  __tablename__ = "Responsaveis"

  id_responsavel: Mapped[int] = mapped_column(init=False, primary_key=True)
  nome: Mapped[str]
  sobrenome: Mapped[str]
  parentesco: Mapped[str]
  cpf: Mapped[str]
  rg: Mapped[str]
  endereco: Mapped[str]
  cep: Mapped[str]
  email: Mapped[str]
  telefone: Mapped[str]
  autorizado_buscar: Mapped[bool]

  alunos:Mapped[list["Aluno"]] = relationship(init=False, back_populates="responsavel", default_factory=list)

@table_registry.mapped_as_dataclass
class Professores:
  __tablename__ = "Professores"

  id_professor: Mapped[int] = mapped_column(init=False, primary_key=True)
  nome: Mapped[str]
  sobrenome: Mapped[str]
  data_nascimento: Mapped[date]
  sexo: Mapped[str]
  cpf: Mapped[str]
  rg: Mapped[str]
  endereco: Mapped[str]
  telefone: Mapped[str]
  email: Mapped[str]
  data_admissao: Mapped[date] = mapped_column(init=False, server_default=func.now())
  formacao_academica: Mapped[str]
  area_especializacao: Mapped[str] = mapped_column(nullable=False)
  carga_horaria_semanal: Mapped[int]
  status: Mapped[str]

@table_registry.mapped_as_dataclass
class Turmas:
  __tablename__ = "Turmas"

  id_turma: Mapped[int] = mapped_column(init=False, primary_key=True)
  ano_letivo: Mapped[int]
  nome: Mapped[str]
  serie: Mapped[str]
  nivel: Mapped[str]
  turno: Mapped[str]
  capacidade_maxima: Mapped[str]
  total_alunos: Mapped[str]
  status: Mapped[str]

  id_professor_responsavel: Mapped[int] = mapped_column(ForeignKey("Professores.id_professor"))
  id_sala: Mapped[int] = ...


