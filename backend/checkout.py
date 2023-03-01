from models.response import response
from models.auth import validate
from models.Environ import Environ
from models.Database import initialize_db
from models.Book import Book
from models.Receipt import Receipt
from models.User import User
import asyncio
import stripe
import json

stripe.api_key = Environ.STRIPE_KEY

initialize_db([Book, Receipt, User])

# NOTE: users can checkout books
def lambda_handler(event, context):
    return asyncio.get_event_loop().run_until_complete(checkout(event))


async def checkout(event):
    try:
        req_body: dict = json.loads(event["body"])
        req_headers: dict = json.loads(event.get("headers"))
    except:
        req_body: dict = event["body"]
        req_headers: dict = event.get("headers")
    if req_headers is None or req_headers.get("access_token") is None:
        return response(401, {"error": "must be logged in to checkout!"})
    user = await validate(req_headers["access_token"])
    if user is None:
        return response(401, {"error": "must be logged in to checkout!"})

    user_card: dict = {
        "card_num": req_body["card_num"],
        "card_cvc": req_body["card_cvc"],
        "card_exp_month": req_body["card_exp_month"],
        "card_exp_year": req_body["card_exp_year"],
    }

    purchase_info: dict = {
        "email": user.email,
        "books": req_body["books"],
    }

    purchases: dict = {}
    total_price: float = 0.0
    for book_id in purchase_info["books"]:
        book: Book = await Book.get(book_id)
        if book is None:
            return response(404, {"error": f"Book does not exist with id: {book_id}"})
        purchases[book_id] = book.purchase_price
        total_price += float(book.purchase_price)

    try:
        card = stripe.Token.create(
            card={
                "number": user_card["card_num"],
                "exp_month": user_card["card_exp_month"],
                "exp_year": user_card["card_exp_year"],
                "cvc": user_card["card_cvc"],
            },
        )
        amount_due: int = int(total_price * 100)  # works in cents
        charge: stripe.Charge = stripe.Charge.create(
            amount=amount_due, currency="usd", source=card.id
        )
    except stripe.error.CardError as e:
        return response(406, {"Card Error": e.error.message})

    for book_id in purchase_info["books"]:
        book: Book = await Book.get(book_id)
        book.is_available = False
        await book.save()
        user.owned.append(book)
    await user.save()

    receipt: Receipt = Receipt(
        user=user,
        total_price=total_price,
        stripe_payment_id=charge.id,
        purchases=purchases,
    )
    await receipt.save()

    return response(200, {"successfully purchased": receipt.dict()})
