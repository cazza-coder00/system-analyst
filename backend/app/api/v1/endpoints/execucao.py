# backend/app/api/v1/endpoints/execucao.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.core.database import get_db
from app.models import execucao as models
from app.schemas import execucao as schemas

router = APIRouter()

# --- ROTAS PARA CASOS DE TESTE (BDD) ---

@router.post("/testes/", response_model=schemas.CasoTesteResponse, status_code=status.HTTP_201_CREATED)
def criar_caso_teste(teste: schemas.CasoTesteCreate, db: Session = Depends(get_db)):
    """
    Cadastra um novo cenário de teste estruturado em BDD.
    Verifica se o código do teste já existe.
    """
    teste_existente = db.query(models.CasoTeste).filter(models.CasoTeste.codigo == teste.codigo).first()
    if teste_existente:
        raise HTTPException(status_code=400, detail="Código de Caso de Teste já cadastrado.")
    
    db_teste = models.CasoTeste(**teste.model_dump())
    db.add(db_teste)
    db.commit()
    db.refresh(db_teste)
    return db_teste

@router.get("/testes/", response_model=List[schemas.CasoTesteResponse])
def listar_casos_teste(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Lista os casos de teste cadastrados."""
    return db.query(models.CasoTeste).offset(skip).limit(limit).all()


# --- ROTAS PARA MUDANÇAS DE ESCOPO ---

@router.post("/mudancas/", response_model=schemas.MudancaEscopoResponse, status_code=status.HTTP_201_CREATED)
def criar_mudanca_escopo(mudanca: schemas.MudancaEscopoCreate, db: Session = Depends(get_db)):
    """
    Registra uma nova solicitação de mudança de escopo (Change Request).
    """
    db_mudanca = models.MudancaEscopo(**mudanca.model_dump())
    db.add(db_mudanca)
    db.commit()
    db.refresh(db_mudanca)
    return db_mudanca

@router.get("/mudancas/", response_model=List[schemas.MudancaEscopoResponse])
def listar_mudancas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Lista as solicitações de mudança de escopo registradas."""
    return db.query(models.MudancaEscopo).offset(skip).limit(limit).all()