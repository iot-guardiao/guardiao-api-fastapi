from http.client import HTTPResponse
from fastapi import APIRouter, Depends, status, Header
from sqlalchemy.orm import Session

from api._database.connect import get_db
from api.v1.agendamento.service import AgendamentoService
from api.v1.agendamento.shema import AgendamentoCreate, AgendamentoListResponse, AgendamentoResponse

router = APIRouter(prefix="/agendamentos", tags=["Agendamento"])

agendamento_service = AgendamentoService()

@router.get("/", response_model=AgendamentoListResponse)
def listar_agendamentos(db: Session = Depends(get_db)):
    data = agendamento_service.get_all(db)
    return {"agendamentos": data}

@router.post("/")
def criar_agendamento(data: AgendamentoCreate, db: Session = Depends(get_db)):
    agendamento = agendamento_service.create(db, data)
    return agendamento

@router.get("/verificar/{sala_id}/{codigo}/")
def verificar_agendamento(sala_id: str, codigo: str, db: Session = Depends(get_db)):
    agendamento = agendamento_service.verify(db, sala_id, codigo)
    return agendamento