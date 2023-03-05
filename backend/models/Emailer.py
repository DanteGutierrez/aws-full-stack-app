import asyncio
from fastapi_mail import ConnectionConfig, FastMail, MessageSchema, MessageType
from models.Environ import Environ
from models.Database import initialize_db
from models.Receipt import Receipt
from models.User import User
from models.Book import Book


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

initialize_db([Receipt, User, Book])

def send_email(reciept_id: str):
    asyncio.get_event_loop().run_until_complete(async_send_email(reciept_id))

async def format_email(reciept: Receipt, user: User):
    email_body = f'''<h3>{user.name} - {user.email}</h3><div><table><thead>
                <tr>
                    <th>ID</th>
                    <th>Title</th>
                    <th>Genre</th>
                    <th>Author</th>
                    <th>Price</th>
                </tr>
            </thead><tbody>'''
    
    for book_id, price in reciept.purchases.items():
        book: Book = await Book.get(book_id)
        email_body += f'''<tr>
                <td>{book.id}</td>
                <td>{book.title}</td>
                <td>{book.genre}</td>
                <td>{book.author}</td>
                <td>{"${:.2f}".format(price)}</td>
            </tr>'''
        
    email_body += f'''</tbody></table><h3>${reciept.total_price} issued to StripeID:[{reciept.stripe_payment_id}] at {reciept.datetime}</h3></div>'''
    return str(email_body)

async def async_send_email(reciept_id: str):
    reciept: Receipt = await Receipt.get(reciept_id)
    user: User = await User.get(reciept.user_id)
    email_body = await format_email(reciept, user)

    message = MessageSchema(
        subject=f"Book Order for {user.name}",
        recipients=[user.email],
        body=email_body,
        subtype=MessageType.html
    )
    await fastmail.send_message(message)