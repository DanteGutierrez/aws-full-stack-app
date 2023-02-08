from pydantic import BaseModel
from beanie import Document, Link
from typing import Optional
from models.User import User
from models.Book import Book


class Review(Document):
    book: Link[Book]
    user: Link[User]
    rating: int
    review: Optional[str]


class ReviewIn(BaseModel):
    user_id: str
    book_id: str
    rating: int
    review: Optional[str]
