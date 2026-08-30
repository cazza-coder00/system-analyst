# backend/app/models/modelagem.py

from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

# Tabela de Processos de Negócio (As-Is / To-Be)
class ProcessoBPMN(Base):
    __tablename__ = "processos_bpmn"
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    descricao = Column(Text)
    link_diagrama = Column(String(255), nullable=False) # URL para o fluxograma
    
    # Chave Estrangeira: Vincula o processo a um Requisito do Módulo 1
    requisito_id = Column(Integer, ForeignKey("requisitos.id"))
    requisito = relationship("Requisito")

# Tabela de Repositório de Telas (Wireframes)
class TelaWireframe(Base):
    __tablename__ = "telas_wireframe"
    
    id = Column(Integer, primary_key=True, index=True)
    codigo = Column(String(20), unique=True, index=True) # Ex: TELA-01
    nome = Column(String(100), nullable=False)
    link_prototipo = Column(String(255), nullable=False) # URL do Figma/Axure
    
    # Chave Estrangeira: Vincula a tela a uma User Story do Módulo 1
    user_story_id = Column(Integer, ForeignKey("user_stories.id"))
    user_story = relationship("UserStory")