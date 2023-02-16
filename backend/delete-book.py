from models.Database import initialize_db, connect_db
from models.response import response
from models.Book import Book, Genre, Condition
import asyncio

initialize_db([Book])

# NOTE: only admins can delete books
def lambda_handler(event, context):

    return asyncio.get_event_loop().run_until_complete(delete_book(event))

async def delete_book(event):

    if "pathParameters" not in event:
        return response(400, {"message":"need to select id"})
    
    path = event["pathParameters"]

    if path is None or "id" not in path:
        return response(400, {"message":"needs id"})
    
    book: Book = await Book.get(path["id"])

    if book is None:
      return response(404, {"message":"entry not found"})
    
    await book.delete()

    return response(200, {})
