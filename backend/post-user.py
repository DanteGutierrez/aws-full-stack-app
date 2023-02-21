from models.response import response
from models.User import User, Role
from models.Database import initialize_db
import asyncio
import json
from bson import json_util

initialize_db([User])

# NOTE: no auth required
def lambda_handler(event, context):
    return asyncio.get_event_loop().run_until_complete(post_user(event))


async def post_user(event):
    try:
        req_body: dict = json.loads(event["body"])
    except:
        req_body: dict = event["body"]
    if req_body.get("role") == "admin":
        user: User = User(
            name=req_body["name"],
            password=req_body["password"],
            email=req_body["email"],
            role=Role.ADMIN,
        )
    else:
        user: User = User(
            name=req_body["name"],
            password=req_body["password"],
            email=req_body["email"],
        )
    await user.create()
    return response(200, json.loads(json_util.dumps(user.dict())))
