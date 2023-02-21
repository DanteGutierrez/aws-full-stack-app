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
    path_params: dict = event.get("pathParameters")
    try:
        if path_params is None:
            return response(200, await User.find_all().to_list())
        if path_params.get("id") is not None:
            user = await User.get(path_params["id"])
            return response(200, user.dict())
        elif path_params.get("email") is not None:
            user = await User.find_one(User.email == path_params["email"])
            return response(200, user.dict())
        else:
            return response(200, await User.find_all().to_list())

    except Exception as e:
        return response(500, str(e))
