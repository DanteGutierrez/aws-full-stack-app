from models.response import response
from models.User import User, Role
from models.Database import initialize_db
import asyncio
import json
from bson import json_util
import jwt

initialize_db([User])

# NOTE: no auth required
def lambda_handler(event, context):
    return asyncio.get_event_loop().run_until_complete(post_login(event))


async def post_login(event):
    try:
        req_body: dict = json.loads(event["body"])
    except:
        req_body: dict = event["body"]
    email: str = req_body["email"]
    password: str = req_body["password"]
    user: User = await User.find_one({"email": email, "password": password})
    if user is None:
        return response(404, {"error": "User does not exist with that email/password"})
    access_token: str = jwt.encode(
        {"bearer_token": user.email}, "secret", algorithm="HS256"
    )
    return response(200, {"access_token": access_token})
