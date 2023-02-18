from models.Database import initialize_db, connect_db
from models.response import response
from models.Book import Book, Genre, Condition
import asyncio

initialize_db([Book])

# NOTE: who can update books? Are we using this endpoint for checking out books?
def lambda_handler(event, context):

    return asyncio.get_event_loop().run_until_complete(put_book(event))

async def put_book(event):

    if "id" not in event:
        return response(400, {"message": "id required"})

    book: Book = await Book.get(event["id"])

    if book is None:
        return response(404, {"message": "entry not found"})

    if "title" in event:
        book.title = event["title"]

    if "pic" in event:
        book.pic = event["pic"]

    if "author" in event:
        book.author = event["author"]

    if ("genre" in event and event["genre"] in Genre._value2member_map_):
        book.genre = event["genre"]

    if "purchase_price" in event:
        book.purchase_price = event["purchase_price"]

    if "rent_price" in event:
        book.rent_price = event["rent_price"]

    if ("condition" in event and event["condition"] in Condition._value2member_map_):
        book.condition = event["condition"]

    if "description" in event:
        book.description = event["description"]

    if "is_paperback" in event:
        book.is_paperback = event["is_paperback"]
        
    if "is_available" in event:
        book.is_available = event["is_available"]

    savedBook = await book.save()

    return response(200, savedBook.dict())
