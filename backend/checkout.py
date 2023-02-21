from models.response import response
from models.Environ import Environ
import asyncio

# NOTE: users can checkout books
def lambda_handler(event, context):
    return asyncio.get_event_loop().run_until_complete(get_user(event))


async def get_user(event):
    return response(200, {"stripe_key": Environ.STRIPE_KEY})
