from datetime import date, time
from pydantic import BaseModel

class AgendamentoCreate(BaseModel):
    responsavel: str
    sala: str
    data: date
    hora_inicio: time
    hora_fim: time
    email: str
    
    class Config:
        orm_mode = True
    
class AgendamentoResponse(BaseModel):
    id: int
    responsavel: str
    sala: str
    data: date
    hora_inicio: time
    hora_fim: time
    email: str
    codigo: str
    
    class Config:
        orm_mode = True
        
class AgendamentoListResponse(BaseModel):
    agendamentos: list[AgendamentoResponse]
    
    class Config:
        orm_mode = True
