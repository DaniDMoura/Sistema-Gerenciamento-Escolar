from sqlalchemy.orm import Mapped, mapped_column, registry, relationship
from datetime import date, datetime
from sqlalchemy import ForeignKey, func

table_registry = registry()


@table_registry.mapped_as_dataclass
class Alunos:
    __tablename__ = 'Alunos'

    id_aluno: Mapped[int] = mapped_column(init=False, primary_key=True)
    nome: Mapped[str] = mapped_column(index=True)
    sobrenome: Mapped[str] = mapped_column(index=True)
    data_nascimento: Mapped[date]
    sexo: Mapped[str]
    cpf: Mapped[str] = mapped_column(unique=True)
    rg: Mapped[str] = mapped_column(unique=True)
    endereco: Mapped[str]
    cep: Mapped[str]
    email: Mapped[str] = mapped_column(index=True)
    telefone: Mapped[str] = mapped_column(index=True)
    foto: Mapped[str] = mapped_column(nullable=True)
    status: Mapped[str]
    necessidades: Mapped[str] = mapped_column(nullable=True)
    grupo_sanguineo: Mapped[str] = mapped_column(nullable=True)
    medicamentos: Mapped[str] = mapped_column(nullable=True)

    id_responsavel: Mapped[int] = mapped_column(
        ForeignKey('Responsaveis.id_responsavel'), nullable=True
    )
    responsavel: Mapped['Responsaveis'] = relationship(
        init=False, back_populates='alunos'
    )

    notas: Mapped[list['Notas']] = relationship(
        init=False, back_populates='aluno', default_factory=list
    )
    frequencias: Mapped[list['Frequencias']] = relationship(
        init=False, back_populates='aluno', default_factory=list
    )


@table_registry.mapped_as_dataclass
class Responsaveis:
    __tablename__ = 'Responsaveis'

    id_responsavel: Mapped[int] = mapped_column(init=False, primary_key=True)
    nome: Mapped[str] = mapped_column(index=True)
    sobrenome: Mapped[str] = mapped_column(index=True)
    parentesco: Mapped[str] = mapped_column(nullable=True)
    cpf: Mapped[str]
    rg: Mapped[str]
    endereco: Mapped[str]
    cep: Mapped[str]
    email: Mapped[str] = mapped_column(index=True)
    telefone: Mapped[str]
    autorizado_buscar: Mapped[bool]

    alunos: Mapped[list['Alunos']] = relationship(
        init=False, back_populates='responsavel', default_factory=list
    )


@table_registry.mapped_as_dataclass
class Professores:
    __tablename__ = 'Professores'

    id_professor: Mapped[int] = mapped_column(init=False, primary_key=True)
    nome: Mapped[str] = mapped_column(index=True)
    sobrenome: Mapped[str] = mapped_column(index=True)
    data_nascimento: Mapped[date]
    sexo: Mapped[str]
    cpf: Mapped[str]
    rg: Mapped[str]
    endereco: Mapped[str]
    telefone: Mapped[str] = mapped_column(index=True)
    email: Mapped[str] = mapped_column(index=True)
    data_admissao: Mapped[date] = mapped_column(
        init=False, server_default=func.now()
    )
    formacao_academica: Mapped[str]
    area_especializacao: Mapped[str]
    carga_horaria_semanal: Mapped[int]
    status: Mapped[str]
    foto: Mapped[str] = mapped_column(nullable=True)

    alocacoes: Mapped[list['Alocacoes']] = relationship(
        init=False, back_populates='professor', default_factory=list
    )


@table_registry.mapped_as_dataclass
class Turmas:
    __tablename__ = 'Turmas'

    id_turma: Mapped[int] = mapped_column(init=False, primary_key=True)
    ano_letivo: Mapped[int]
    nome: Mapped[str] = mapped_column(index=True)
    serie: Mapped[str]
    nivel: Mapped[str]
    turno: Mapped[str]
    capacidade_maxima: Mapped[int] = mapped_column(nullable=True)
    status: Mapped[str]

    alocacoes: Mapped[list['Alocacoes']] = relationship(
        init=False, back_populates='turma', default_factory=list
    )


@table_registry.mapped_as_dataclass
class Disciplinas:
    __tablename__ = 'Disciplinas'

    id_disciplina: Mapped[int] = mapped_column(init=False, primary_key=True)
    nome: Mapped[str] = mapped_column(index=True)
    descricao: Mapped[str]
    carga_horaria: Mapped[int]
    nivel: Mapped[str] = mapped_column(index=True)
    area_conhecimento: Mapped[str]
    obrigatoria: Mapped[bool]

    alocacoes: Mapped[list['Alocacoes']] = relationship(
        init=False, back_populates='disciplina', default_factory=list
    )
    notas: Mapped[list['Notas']] = relationship(
        init=False, back_populates='disciplina', default_factory=list
    )
    frequencias: Mapped[list['Frequencias']] = relationship(
        init=False, back_populates='disciplina', default_factory=list
    )


@table_registry.mapped_as_dataclass
class Alocacoes:
    __tablename__ = 'Alocacoes'

    id_alocacao: Mapped[int] = mapped_column(init=False, primary_key=True)
    id_professor: Mapped[int] = mapped_column(
        ForeignKey('Professores.id_professor')
    )
    id_disciplina: Mapped[int] = mapped_column(
        ForeignKey('Disciplinas.id_disciplina')
    )
    id_turma: Mapped[int] = mapped_column(ForeignKey('Turmas.id_turma'))

    professor: Mapped['Professores'] = relationship(
        init=False, back_populates='alocacoes'
    )
    disciplina: Mapped['Disciplinas'] = relationship(
        init=False, back_populates='alocacoes'
    )
    turma: Mapped['Turmas'] = relationship(
        init=False, back_populates='alocacoes'
    )


@table_registry.mapped_as_dataclass
class Notas:
    __tablename__ = 'Notas'

    id_nota: Mapped[int] = mapped_column(init=False, primary_key=True)
    id_aluno: Mapped[int] = mapped_column(ForeignKey('Alunos.id_aluno'))
    id_disciplina: Mapped[int] = mapped_column(
        ForeignKey('Disciplinas.id_disciplina')
    )
    bimestre: Mapped[int]
    valor: Mapped[float]
    data_lancamento: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now()
    )

    aluno: Mapped['Alunos'] = relationship(init=False, back_populates='notas')
    disciplina: Mapped['Disciplinas'] = relationship(
        init=False, back_populates='notas'
    )


@table_registry.mapped_as_dataclass
class Frequencias:
    __tablename__ = 'Frequencias'

    id_frequencia: Mapped[int] = mapped_column(init=False, primary_key=True)
    id_aluno: Mapped[int] = mapped_column(ForeignKey('Alunos.id_aluno'))
    id_disciplina: Mapped[int] = mapped_column(
        ForeignKey('Disciplinas.id_disciplina')
    )
    data: Mapped[date]
    presente: Mapped[bool]

    aluno: Mapped['Alunos'] = relationship(
        init=False, back_populates='frequencias'
    )
    disciplina: Mapped['Disciplinas'] = relationship(
        init=False, back_populates='frequencias'
    )
