from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
import asyncio
from models.Environ import Environ


async def connect_db(models: list):
    """Initialize db service"""
    client = AsyncIOMotorClient(Environ.MONGO_CON)
    await init_beanie(database=client.Booked_Store, document_models=models)


def initialize_db(models: list):
    asyncio.get_event_loop().run_until_complete(connect_db(models))
