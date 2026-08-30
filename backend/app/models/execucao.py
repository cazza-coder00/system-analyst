# backend/app/models/execucao.py

from sqlalchemy import Column, Integer, String, Text, ForeignKey, Enum
from sqlalchemy.orm import relationship
import enum
from app.core.database import Base

# Enum para padronizar o status de homologação
class StatusTeste(str, enum.Enum):
    PENDENTE = "Pendente"
    APROVADO = "Aprovado"
    REPROVADO = "Reprovado"

# Tabela de Critérios de Aceite (BDD - Behavior Driven Development)
class CasoTeste(Base):
    __tablename__ = "casos_teste"
    
    id = Column(Integer, primary_key=True, index=True)
    codigo = Column(String(20), unique=True, index=True, nullable=False) # Ex: CT-01
    cenario = Column(String(150), nullable=False)
    
    # Estrutura BDD
    dado_que = Column(Text, nullable=False) # Contexto inicial
    quando = Column(Text, nullable=False)   # Ação executada
    entao = Column(Text, nullable=False)    # Resultado esperado
    
    status = Column(Enum(StatusTeste), default=StatusTeste.PENDENTE)
    
    # Chave Estrangeira: Vincula o teste à User Story correspondente no Módulo 1
    user_story_id = Column(Integer, ForeignKey("user_stories.id"))
    user_story = relationship("UserStory")

# Tabela de Gestão de Mudanças (Change Request)
class MudancaEscopo(Base):
    __tablename__ = "mudancas_escopo"
    
    id = Column(Integer, primary_key=True, index=True)
    motivo = Column(Text, nullable=False)
    impacto_estimado = Column(String(100)) # Ex: "Alto - Refatoração de Tela"
    status_aprovacao = Column(String(50), default="Em Análise")
    
    # Chave Estrangeira: Identifica qual Requisito (Módulo 1) sofrerá a alteração
    requisito_id = Column(Integer, ForeignKey("requisitos.id"))
    requisito = relationship("Requisito")