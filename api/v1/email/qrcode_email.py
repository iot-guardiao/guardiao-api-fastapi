import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import smtplib
from dotenv import load_dotenv

load_dotenv()

SMTP_SERVER = os.getenv("SMTP_SERVER")
PORT = os.getenv("PORT")
LOGIN = os.getenv("LOGIN_EMAIL")
PASSWORD = os.getenv("LOGIN_PASSWORD")

def send_email_with_qrcode(qr_code_file, recipient_email, responsavel, sala, horario, data):
    sender_email = LOGIN

    # Create the email object
    message = MIMEMultipart("alternative")
    message["Subject"] = "📅 Agendamento Confirmado! Seu QR Code está pronto 🏷️"
    message["From"] = sender_email
    message["To"] = recipient_email

    # HTML content for the email body
    html_body = f"""
    <html>
    <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
        <div style="max-width: 600px; margin: auto; border: 1px solid #ddd; border-radius: 8px; padding: 20px; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);">
            <h2 style="text-align: center; color: #4CAF50;">✅ Agendamento Confirmado!</h2>
            <p>Olá <b>{responsavel}</b>,</p>
            <p>Seu agendamento foi cadastrado com sucesso. Aqui estão os detalhes:</p>
            <ul style="list-style-type: none; padding: 0;">
                <li><b>Sala:</b> {sala}</li>
                <li><b>Horário:</b> {horario}</li>
                <li><b>Data:</b> {data}</li>
            </ul>
            <p style="margin-top: 20px;">Utilize o QR Code em anexo para solicitar a entrada na sala <b>{sala}</b>. Certifique-se de tê-lo disponível no dia do agendamento.</p>
            <div style="text-align: center; margin-top: 30px;">
                <p style="font-size: 14px; color: #888;">Se você tiver dúvidas, entre em contato com a nossa equipe de suporte.</p>
            </div>
            <footer style="margin-top: 20px; text-align: center; color: #666; font-size: 12px;">
                <p>© 2025 Guardião. Todos os direitos reservados.</p>
            </footer>
        </div>
    </body>
    </html>
    """

    # Attach HTML body to the email
    message.attach(MIMEText(html_body, "html"))

    # Attach the QR code file
    with open(qr_code_file, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
    
    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition",
        f"attachment; filename={os.path.basename(qr_code_file)}",
    )
    message.attach(part)

    # Send the email
    try:
        with smtplib.SMTP(SMTP_SERVER, PORT) as server:
            server.starttls()
            server.login(LOGIN, PASSWORD)
            server.sendmail(sender_email, recipient_email, message.as_string())
        print("E-mail enviado com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")