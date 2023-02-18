from models.Database import initialize_db, connect_db
from models.response import response
from models.Book import Book, Genre, Condition
import asyncio

initialize_db([Book])

# NOTE: only admins can post books
def lambda_handler(event, context):

    return asyncio.get_event_loop().run_until_complete(post_book(event))

async def post_book(event):

    if ("title" not in event 
        or "pic" not in event 
        or "author" not in event 
        or ("genre" not in event and event["genre"] not in Genre._value2member_map_)
        or "purchase_price" not in event
        or "rent_price" not in event
        or ("condition" not in event and event["condition"] not in Condition._value2member_map_)
        or "description" not in event
        or "is_paperback" not in event):

        return response(400, {"message": "Book missing data"})
    

    book = Book(
        title=event["title"],
        pic=event["pic"],
        author=event["author"],
        genre=event["genre"],
        purchase_price=event["purchase_price"],
        rent_price=event["rent_price"],
        condition=event["condition"],
        description=event["description"],
        is_paperback=event["is_paperback"],
        is_available=True,
    )

    savedBook = await book.save()

    return response(200, savedBook.dict())
