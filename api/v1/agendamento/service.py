from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import uuid
from sqlalchemy.orm import Session

from api._database.models import Agendamento
from api.utils.exceptions import ExceptionConflict
from api.utils.sqlalchemy_errors import handle_sqlalchemy_errors
from api.v1.agendamento.shema import AgendamentoCreate
import os
from dotenv import load_dotenv
load_dotenv()

SMTP_SERVER = "smtp.gmail.com"
PORT = 587
LOGIN = os.getenv("LOGIN_EMAIL")
PASSWORD = os.getenv("LOGIN_PASSWORD")

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
        
        self.send_email(data.email)
        
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
    
    def send_email(self, receiver_email: str):
        sender_email = LOGIN

        html = """\
            <html>
            <body>
                <p>Hi,<br>
                This is the test email</p>
            </body>
            </html>
        """
        message = MIMEMultipart("alternative")
        message["Subject"] = "Test subject"
        message["From"] = sender_email
        message["To"] = receiver_email
        part = MIMEText(html, "html")
        message.attach(part)

        try:
            with smtplib.SMTP(SMTP_SERVER, PORT) as server:
                server.starttls()
                server.login(LOGIN, PASSWORD)
                server.sendmail(sender_email, receiver_email, message.as_string())
            return {"msg": "Email enviado com sucesso!"}
        except Exception as e:
            return {"msg": f"Erro ao enviar email: {e}"}