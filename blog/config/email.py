from fastapi import FastAPI, BackgroundTasks
from email.message import EmailMessage
import smtplib
import ssl

from email.message import EmailMessage
from email.utils import make_msgid
import smtplib

EMAIL_SENDER = "akshaysethiya0904@gmail.com"
EMAIL_PASSWORD = "xstqgjanqoonhdzb"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

def send_email(to_email: str, subject: str, body: str):
    msg = EmailMessage()
    msg["From"] = f"Akshay <{EMAIL_SENDER}>"
    msg["To"] = to_email
    msg["Subject"] = subject
    msg["Reply-To"] = EMAIL_SENDER
    msg["Message-ID"] = make_msgid()

    msg.set_content("Your email client does not support HTML")

    msg.add_alternative(f"""
    <html>
      <body>
        <h2>{subject}</h2>
        <p>{body}</p>
        <br>
        <p>Regards,<br>Akshay</p>
      </body>
    </html>
    """, subtype="html")

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.send_message(msg)
