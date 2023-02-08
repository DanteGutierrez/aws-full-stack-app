from pydantic import Field, BaseModel
from beanie import Document
from enum import Enum
from decimal import Decimal


class Genre(str, Enum):
    FICTION = "Fiction"
    NON_FICTION = "Non-Fiction"
    SCIENCE_FICTION = "Science Fiction"
    FANTASY = "Fantasy"
    HORROR = "Horror"
    ROMANCE = "Romance"


class Condition(str, Enum):
    MINT_CONDITION = "Mint Condition"
    GOOD_CONDITION = "Good Condition"
    FAIR_CONDITION = "Fair Condition"
    POOR_CONDITION = "Poor Condition"


class Book(Document, BaseModel):
    title: str
    pic: str
    author: str
    genre: Genre
    purchase_price: Decimal = Field(decimal_places=2)
    rent_price: Decimal = Field(decimal_places=2)
    condition: Condition
    description: str
    is_paperback: bool
    is_available: bool = Field(default=True)
    # owner: Optional[str]  # grab owner from user backwards linking
