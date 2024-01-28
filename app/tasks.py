from celery import Celery
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

@Celery.task
def send_email(recipient, subject, body):
    sender = "teste@gmail.com"
    password = "123456teste"

    smtp_server = "smtp.example.com"
    port = 587

    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = sender
    message["To"] = recipient

    text = MIMEText(body, "plain")
    message.attach(text)

    try:
        server = smtplib.SMTP(smtp_server, port)
        server.starttls() 
        server.login(sender, password)
        server.sendmail(sender, recipient, message.as_string())
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")
    finally:
        server.quit()
