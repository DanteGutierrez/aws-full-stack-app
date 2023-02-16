from models.Database import initialize_db, connect_db
from models.response import response
from models.Book import Book, Genre, Condition
import asyncio

initialize_db([Book])

# NOTE: users and admins can get books
def lambda_handler(event, context):

    return asyncio.get_event_loop().run_until_complete(get_books(event))

async def get_books(event):

    if "pathParameters" not in event or "queryStringParameters" not in event:
        return response(400, {"message": "missing request data"})

    path = event["pathParameters"]

    if path is not None and "id" in path:
        
        book: Book = await Book.get(path["id"])

        if book is None:
            return response(404, {"message": "object not found"})

        return response(200, book.dict())

    params = event["queryStringParameters"]

    bookList = await Book.find_all().to_list()

    resultList = []

    for book in bookList:
        
        if params is None or book_validity(book, params):

            resultList.append(book.dict())

    return response(200, resultList)


def book_validity(book, params):
    valid = True

    if "title" in params and params["title"] not in book.title:
        valid = False

    if "author" in params and params["author"] not in book.author:
        valid = False

    if "genre" in params and params["genre"] not in book.genre:
        valid = False

    if "condition" in params and params["condition"] not in book.condition:
        valid = False

    if "is_paperback" in params and params["is_paperback"] == book.is_paperback:
        valid = False

    if "is_available" in params and params["is_available"] == book.is_available:
        valid = False

    if "price_minimum" in params and book.purchase_price < params["price_minimum"] and book.rent_price < params["price_minimum"]:
        valid = False

    if "price_maximum" in params and book.purchase_price > params["price_maximum"] and book.rent_price > params["price_maximum"]:
        valid = False

    return valid