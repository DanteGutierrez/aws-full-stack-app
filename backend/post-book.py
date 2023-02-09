from models.Database import initialize_db, connect_db
from models.response import response
from models.Book import Book, Genre, Condition
import asyncio

# asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
# asyncio.new_event_loop()

# NOTE: only admins can post books
def lambda_handler(event, context):
    print("starting...")
    asyncio.run(test())
    print("done")
    # TODO implement
    # return response(0, {})
    return {"fuck": "you"}


# initialize_db([Book])


async def test():
    await connect_db([Book])
    await create_book()


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
    await book.save()

    new_books = await Book.find_all().to_list()
    print(new_books)


# asyncio.run(create_book())
# print("done")
