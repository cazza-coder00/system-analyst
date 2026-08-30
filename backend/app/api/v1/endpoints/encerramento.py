# backend/app/api/v1/endpoints/encerramento.py

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List

from app.core.database import get_db
from app.models import encerramento as models
from app.schemas import encerramento as schemas

router = APIRouter()

# --- ROTAS PARA TERMOS DE ACEITE ---

@router.post("/termos/", response_model=schemas.TermoAceiteResponse, status_code=status.HTTP_201_CREATED)
def criar_termo_aceite(termo: schemas.TermoAceiteCreate, db: Session = Depends(get_db)):
    """
    Cadastra um novo Termo de Aceite validado por um stakeholder.
    """
    db_termo = models.TermoAceite(**termo.model_dump())
    db.add(db_termo)
    db.commit()
    db.refresh(db_termo)
    return db_termo

@router.get("/termos/", response_model=List[schemas.TermoAceiteResponse])
def listar_termos_aceite(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Lista os termos de aceite emitidos."""
    return db.query(models.TermoAceite).offset(skip).limit(limit).all()


# --- ROTAS PARA LIÇÕES APRENDIDAS ---

@router.post("/licoes/", response_model=schemas.LicaoAprendidaResponse, status_code=status.HTTP_201_CREATED)
def criar_licao_aprendida(licao: schemas.LicaoAprendidaCreate, db: Session = Depends(get_db)):
    """
    Cadastra uma nova lição aprendida na base de conhecimento.
    """
    db_licao = models.LicaoAprendida(**licao.model_dump())
    db.add(db_licao)
    db.commit()
    db.refresh(db_licao)
    return db_licao

@router.get("/licoes/", response_model=List[schemas.LicaoAprendidaResponse])
def listar_licoes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Lista o histórico de lições aprendidas."""
    return db.query(models.LicaoAprendida).offset(skip).limit(limit).all()