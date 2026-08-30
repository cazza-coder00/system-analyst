# backend/app/models/iniciacao.py

from sqlalchemy import Column, Integer, String, Text, ForeignKey, Enum
from sqlalchemy.orm import relationship
import enum
from app.core.database import Base

# Enums para padronizar as opções de preenchimento no banco de dados
class TipoRequisito(str, enum.Enum):
    FUNCIONAL = "Funcional"
    NAO_FUNCIONAL = "Não Funcional"
    REGRA_NEGOCIO = "Regra de Negócio"

class Prioridade(str, enum.Enum):
    BAIXA = "Baixa"
    MEDIA = "Média"
    ALTA = "Alta"

# Tabela de Stakeholders (Partes Interessadas)
class Stakeholder(Base):
    __tablename__ = "stakeholders"
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    papel = Column(String(100), nullable=False)
    expectativa = Column(Text)
    nivel_poder_interesse = Column(String(50)) # Ex: Alto Poder / Baixo Interesse
    
    # Relacionamento: 1 Stakeholder é responsável por N Requisitos
    requisitos = relationship("Requisito", back_populates="responsavel")

# Tabela do Glossário de Domínio
class Glossario(Base):
    __tablename__ = "glossario"
    
    id = Column(Integer, primary_key=True, index=True)
    termo = Column(String(100), unique=True, index=True, nullable=False)
    definicao = Column(Text, nullable=False)
    contexto_negocio = Column(String(200))

# Tabela de Requisitos (Funcionais, Não Funcionais e Regras)
class Requisito(Base):
    __tablename__ = "requisitos"
    
    id = Column(Integer, primary_key=True, index=True)
    codigo = Column(String(20), unique=True, index=True, nullable=False) # Ex: RF01
    tipo = Column(Enum(TipoRequisito), nullable=False)
    descricao = Column(Text, nullable=False)
    prioridade = Column(Enum(Prioridade), nullable=False)
    status = Column(String(50), default="Em Levantamento")
    
    # Chave Estrangeira: Vincula o requisito a um Stakeholder específico
    stakeholder_id = Column(Integer, ForeignKey("stakeholders.id"))
    responsavel = relationship("Stakeholder", back_populates="requisitos")
    
    # Relacionamento: 1 Requisito pode gerar N User Stories
    user_stories = relationship("UserStory", back_populates="requisito")

# Tabela de User Stories geradas a partir dos Requisitos
class UserStory(Base):
    __tablename__ = "user_stories"
    
    id = Column(Integer, primary_key=True, index=True)
    codigo = Column(String(20), unique=True, index=True, nullable=False) # Ex: US01
    ator = Column(String(100), nullable=False)
    acao = Column(Text, nullable=False)
    beneficio = Column(Text, nullable=False)
    criterio_aceite = Column(Text)
    
    # Chave Estrangeira: Vincula a User Story ao seu Requisito pai
    requisito_id = Column(Integer, ForeignKey("requisitos.id"))
    requisito = relationship("Requisito", back_populates="user_stories")