from pydantic import Field
from beanie import Document, Link
from decimal import Decimal
from typing import Dict, List
from datetime import datetime
from models.User import User


class Receipt(Document):
    user: Link[User]
    datetime: str = Field(default=datetime.now().strftime("%m/%d/%Y %H:%M:%S"))
    total_price: Decimal = Field(decimal_places=2)
    stripe_payment_id: str
    # purchases: Dict[str, List[str]]  # {book_id: [price, rented/owned]}
    purchases: Dict[str, float]  # {book_id: price}
