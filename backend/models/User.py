from pydantic import Field, BaseModel
from beanie import Document, Link
from enum import Enum
from typing import List
from models.Book import Book


class Role(str, Enum):
    USER = "user"
    ADMIN = "admin"


class User(Document, BaseModel):
    name: str
    password: str
    email: str
    role: Role = Field(default=Role.USER)
    rented: List[Link[Book]] = Field(default=[])
    owned: List[Link[Book]] = Field(default=[])
