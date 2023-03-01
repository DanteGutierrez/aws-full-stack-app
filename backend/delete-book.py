from models.Database import initialize_db, connect_db
from models.auth import validate
from models.response import response
from models.Book import Book, Genre, Condition
from models.User import User, Role
import asyncio
import json

initialize_db([Book])

# NOTE: only admins can delete books
def lambda_handler(event, context):

    return asyncio.get_event_loop().run_until_complete(delete_book(event))


async def delete_book(event):
    try:
        req_headers: dict = json.loads(event.get("headers"))
    except:
        req_headers: dict = event.get("headers")
    if req_headers is None or req_headers.get("access_token") is None:
        return response(401, {"error": "must be logged in to delete book"})
    user = await validate(req_headers["access_token"])
    if user is None:
        return response(401, {"error": "must be logged in to delete book"})
    if user.role != Role.ADMIN:
        return response(403, {"error": "must be admin to delete book"})

    if "pathParameters" not in event:
        return response(400, {"message": "need to select id"})

    path = event["pathParameters"]

    if path is None or "id" not in path:
        return response(400, {"message": "needs id"})

    book: Book = await Book.get(path["id"])

    if book is None:
        return response(404, {"message": "entry not found"})

    await book.delete()

    return response(200, {})
