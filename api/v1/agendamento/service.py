import uuid
from datetime import datetime
from sqlalchemy.orm import Session
from api._database.models import Agendamento
from api.utils.exceptions import ExceptionConflict
from api.v1.agendamento.shema import AgendamentoCreate
from api.v1.email.qrcode_image import generate_qr_code
from api.v1.email.qrcode_email import send_email_with_qrcode
from api.utils.sqlalchemy_errors import handle_sqlalchemy_errors

class AgendamentoService:
    
    def get_all(self, db: Session):
        return db.query(Agendamento).filter(Agendamento.flg_excluido == False).all()
    
    @handle_sqlalchemy_errors
    def create(self, db: Session, data: AgendamentoCreate):
        
        agendamento_duplicado = db.query(Agendamento).filter(
            Agendamento.sala == data.sala,
            Agendamento.data == data.data,
            Agendamento.hora_inicio == data.hora_inicio,
            Agendamento.hora_fim == data.hora_fim,
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
        
        generate_qr_code(codigo_uuid, f"api/v1/agendamento/qrcodes/{codigo_uuid}.png")
        
        send_email_with_qrcode(
            f"api/v1/agendamento/qrcodes/{codigo_uuid}.png",
            data.email,
            data.responsavel,
            data.sala,
            f"{data.hora_inicio} - {data.hora_fim}",
            data.data
        )
        
        db.add(agendamento)
        db.commit()
        db.refresh(agendamento)
        return agendamento

    
    @handle_sqlalchemy_errors
    def verify(self, db: Session, sala_id: int, codigo: str):
        agendamento = db.query(Agendamento).filter(
            Agendamento.sala == sala_id,
            Agendamento.codigo == codigo,
            Agendamento.data == datetime.now().date(),
            Agendamento.hora_inicio <= datetime.now().time(),
            Agendamento.hora_fim >= datetime.now().time(),
        ).first()        
        
        if not agendamento:
            raise ExceptionConflict("Agendamento não encontrado.")
        
        if agendamento:
            return True
        return False