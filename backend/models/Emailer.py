import asyncio
from fastapi_mail import ConnectionConfig, FastMail, MessageSchema, MessageType
from models.Environ import Environ
from models.Database import initialize_db
from models.Receipt import Receipt
from models.User import User


conf = ConnectionConfig(
    MAIL_USERNAME=Environ.MAIL_FROM,
    MAIL_PASSWORD=Environ.MAIL_PASSWORD,
    MAIL_FROM=Environ.MAIL_FROM,
    MAIL_PORT=587,
    MAIL_SERVER='smtp.gmail.com',
    MAIL_STARTTLS = True,
    MAIL_SSL_TLS = False,
    USE_CREDENTIALS = True,
    VALIDATE_CERTS = True
)

fastmail = FastMail(conf)

initialize_db([Receipt, User])

def send_email(reciept_id: str):
    asyncio.get_event_loop().run_until_complete(async_send_email(reciept_id))

async def async_send_email(reciept_id: str):
    reciept: Receipt = await Receipt.get(reciept_id)
    user: User = await User.get(reciept.user_id)
    email = user.email
    
    email_body = str(reciept.purchases)
    # TODO: format email body html

    message = MessageSchema(
        subject=f"Reciept to {email}",
        recipients=[email],
        body=email_body,
        subtype=MessageType.html
    )
    await fastmail.send_message(message)