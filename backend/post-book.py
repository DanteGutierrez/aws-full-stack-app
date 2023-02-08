from models.Database import initialize_db
from models.Response import response
from models.Book import Book, Genre, Condition
import asyncio

# NOTE: only admins can post books
def lambda_handler(event, context):
    # TODO implement
    return response(0, {})


initialize_db([Book])


async def create_book():
    book = Book(
        title="test",
        pic="test",
        author="test",
        genre=Genre.FICTION,
        purchase_price=10.69,
        rent_price=0.69,
        condition=Condition.MINT_CONDITION,
        description="test",
        is_paperback=True,
        is_available=True,
    )
    book.save()


asyncio.run(create_book())
print("done")
