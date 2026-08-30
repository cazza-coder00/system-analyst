# backend/app/api/v1/endpoints/iniciacao.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

# Importa a dependência de banco de dados e os modelos/schemas criados
from app.core.database import get_db
from app.models import iniciacao as models
from app.schemas import iniciacao as schemas

router = APIRouter()

# --- ROTAS PARA STAKEHOLDERS ---

@router.post("/stakeholders/", response_model=schemas.StakeholderResponse, status_code=status.HTTP_201_CREATED)
def criar_stakeholder(stakeholder: schemas.StakeholderCreate, db: Session = Depends(get_db)):
    """
    Cria um novo Stakeholder no banco de dados.
    Recebe os dados validados pelo schema e persiste usando o modelo ORM.
    """
    db_stakeholder = models.Stakeholder(**stakeholder.model_dump())
    db.add(db_stakeholder)
    db.commit()
    db.refresh(db_stakeholder) # Atualiza a instância com o ID gerado pelo banco
    return db_stakeholder

@router.get("/stakeholders/", response_model=List[schemas.StakeholderResponse])
def listar_stakeholders(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Retorna a lista de Stakeholders cadastrados, com paginação básica (skip/limit).
    """
    stakeholders = db.query(models.Stakeholder).offset(skip).limit(limit).all()
    return stakeholders


# --- ROTAS PARA REQUISITOS ---

@router.post("/requisitos/", response_model=schemas.RequisitoResponse, status_code=status.HTTP_201_CREATED)
def criar_requisito(requisito: schemas.RequisitoCreate, db: Session = Depends(get_db)):
    """
    Cria um novo Requisito. Verifica se o código do requisito já existe antes de salvar.
    """
    # Validação de regra de negócio: o código deve ser único
    requisito_existente = db.query(models.Requisito).filter(models.Requisito.codigo == requisito.codigo).first()
    if requisito_existente:
        raise HTTPException(status_code=400, detail="Código de requisito já cadastrado.")
    
    db_requisito = models.Requisito(**requisito.model_dump())
    db.add(db_requisito)
    db.commit()
    db.refresh(db_requisito)
    return db_requisito

@router.get("/requisitos/", response_model=List[schemas.RequisitoResponse])
def listar_requisitos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Retorna a lista de Requisitos.
    """
    requisitos = db.query(models.Requisito).offset(skip).limit(limit).all()
    return requisitos