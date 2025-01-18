import uuid
from sqlalchemy.orm import Session

from api._database.models import Agendamento
from api.utils.exceptions import ExceptionConflict
from api.utils.sqlalchemy_errors import handle_sqlalchemy_errors
from api.v1.agendamento.shema import AgendamentoCreate

class AgendamentoService:
    
    def get_all(self, db: Session):
        return db.query(Agendamento).filter(Agendamento.flg_excluido == False).all()
    
    @handle_sqlalchemy_errors
    def create(self, db: Session, data: AgendamentoCreate):
        
        agendamento_duplicado = db.query(Agendamento).filter(
            Agendamento.sala == data.sala,
            Agendamento.data == data.data,
            Agendamento.hora_inicio == data.hora_inicio,
            Agendamento.hora_fim == data.hora_fim
        ).first()
        
        if agendamento_duplicado:
            raise ExceptionConflict("Sala já agendada para o mesmo dia e horário.")
        
        codigo_uuid = str(uuid.uuid4())
        
        agendamento = Agendamento(
            responsavel=data.responsavel,
            sala=data.sala,
            data=data.data,
            hora_inicio=data.hora_inicio,
            hora_fim=data.hora_fim,
            email=data.email,
            codigo=codigo_uuid  
        )
        db.add(agendamento)
        db.commit()
        db.refresh(agendamento)
        return agendamento