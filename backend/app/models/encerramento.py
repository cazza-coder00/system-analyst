# backend/app/models/encerramento.py

from sqlalchemy import Column, Integer, String, Text, ForeignKey, Date
from sqlalchemy.orm import relationship
import datetime
from app.core.database import Base

# Tabela de Termo de Aceite (Validação de Entregas)
class TermoAceite(Base):
    __tablename__ = "termos_aceite"
    
    id = Column(Integer, primary_key=True, index=True)
    titulo_entrega = Column(String(150), nullable=False) # Ex: "Módulo Financeiro Finalizado"
    data_emissao = Column(Date, default=datetime.date.today)
    status = Column(String(50), default="Aguardando Assinatura")
    
    # Chave Estrangeira: Quem é o Stakeholder (Módulo 1) que está aprovando esta entrega
    stakeholder_id = Column(Integer, ForeignKey("stakeholders.id"))
    stakeholder = relationship("Stakeholder")

# Tabela de Lições Aprendidas (Base de Conhecimento)
class LicaoAprendida(Base):
    __tablename__ = "licoes_aprendidas"
    
    id = Column(Integer, primary_key=True, index=True)
    categoria = Column(String(50), nullable=False) # Ex: "Ponto Positivo", "Ponto de Melhoria", "Gargalo"
    descricao_fato = Column(Text, nullable=False)  # O que aconteceu durante o projeto
    acao_recomendada = Column(Text)                # O que fazer em projetos futuros para evitar/repetir