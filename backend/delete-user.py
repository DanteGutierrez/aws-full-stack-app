from models.response import response
from models.User import User, Role
from models.Database import initialize_db
from models.auth import validate
import asyncio
import json
from bson import json_util

initialize_db([User])

# NOTE: who can get users?
def lambda_handler(event, context):
    return asyncio.get_event_loop().run_until_complete(delete_user(event))


async def delete_user(event):
    try:
        req_body: dict = json.loads(event["body"])
        req_headers: dict = json.loads(event.get("headers"))
    except:
        req_body: dict = event["body"]
        req_headers: dict = event.get("headers")
    if req_headers is None or req_headers.get("access_token") is None:
        return response(401, {"error": "must be logged in to delete user"})
    userVal = await validate(req_headers["access_token"])
    if userVal is None:
        return response(401, {"error": "must be logged in to delete user"})
    if userVal.role != Role.ADMIN:
        return response(403, {"error": "must be admin to delete user"})
    try:
        if req_body.get("id") is not None:
            user = await User.get(req_body["id"])
            if user is None:
                return response(404, {"error": "user not found"})
            await user.delete()
            return response(200, user.dict())
        elif req_body.get("email") is not None:
            user = await User.find_one(User.email == req_body["email"])
            if user is None:
                return response(404, {"error": "user not found"})
            await user.delete()
            return response(200, user.dict())
        else:
            return response(400, json.loads({"error": "must pass in id or email"}))

    except Exception as e:
        return response(500, str(e))
