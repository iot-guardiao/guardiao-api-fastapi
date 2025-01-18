from datetime import datetime, timezone
from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy import Column, Date, DateTime, String, Integer, Time, func, Boolean as Bool

@as_declarative()
class Base:
    id = Column(Integer, primary_key=True, index=True)
    flg_ativo = Column(Bool, index=True, default=True)
    flg_excluido = Column(Bool, index=True, default=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc), nullable=False)
    deleted_at = Column(DateTime, default=func.now())

class Agendamento(Base):
    __tablename__ = "agendamento"
    
    responsavel = Column(String, index=True)
    sala = Column(String, index=True)
    data = Column(Date, nullable=False)
    hora_inicio = Column(Time, nullable=False)
    hora_fim = Column(Time, nullable=False)
    email = Column(String, index=True)
    codigo = Column(String, index=True)
