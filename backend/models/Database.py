from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
import asyncio


async def connect_db(models: list):
    """Initialize db service"""
    client = AsyncIOMotorClient(
        "mongodb+srv://aws-lib:I5TUdvhuo66m0z8h@cluster0.tvvggns.mongodb.net/?retryWrites=true&w=majority"
    )  # switch this to environ variable
    await init_beanie(database=client.BookStore, document_models=models)


def initialize_db(models: list):
    asyncio.run(connect_db(models))
