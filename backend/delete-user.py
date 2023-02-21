from models.response import response
from models.User import User, Role
from models.Database import initialize_db
import asyncio
import json
from bson import json_util

initialize_db([User])

# NOTE: who can get users?
def lambda_handler(event, context):
    return asyncio.get_event_loop().run_until_complete(get_user(event))


async def get_user(event):
    try:
        req_body: dict = json.loads(event["body"])
    except:
        req_body: dict = event["body"]
    try:
        if req_body.get("id") is not None:
            user = await User.get(req_body["id"])
            await user.delete()
            return response(200, user.dict())
        elif req_body.get("email") is not None:
            user = await User.find_one(User.email == req_body["email"])
            await user.delete()
            return response(200, user.dict())
        else:
            return response(400, json.loads({"error": "must pass in id or email"}))

    except Exception as e:
        return response(500, str(e))
