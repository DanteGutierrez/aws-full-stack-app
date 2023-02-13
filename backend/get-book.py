from models.Database import initialize_db, connect_db
from models.response import response
from models.Book import Book, Genre, Condition
import asyncio

initialize_db([Book])

global yourmom 

# NOTE: users and admins can get books
def lambda_handler(event, context):

    return asyncio.get_event_loop().run_until_complete(get_books(event))

    

async def get_books(event):

    if "pathParameters" not in event or "queryStringParameters" not in event:
        return response(400, {"message":"missing request data"})
    
    path = event["pathParameters"]

    if path is not None and "id" in path:

        book:Book = await Book.get(path["id"])

        return response(200, book.title)
    
    params = event["queryStringParameters"]

    if params is None:
        return response(200, {})
    
    return response(400, {})

    
    # Full collection here

    # if "title" in params:
    #     # TODO filter by title
    # if "author" in params:
    #     # TODO filter by author
    # if "genre" in params:
    #     # TODO filter by genre
    # if "purchase_price" in params:
    #     # TODO filter by purchase_price
    # if "rent_price" in params:
    #     # TODO filter by rent_price
    # if "condition" in params:
    #     # TODO filter by condition
    # if "is_paperback" in params:
    #     # TODO filter by is_paperback
    # if "is_available" in params:
    #     # TODO filter by is_available

    # # TODO return collection
    # return response(0, {})