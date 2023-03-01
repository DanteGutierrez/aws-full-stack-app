from models.User import User
import jwt


async def validate(access_dict: dict) -> User:
    access_dict = jwt.decode(access_dict, "secret", algorithms=["HS256"])
    user: User = await User.find_one({"email": access_dict["bearer_token"]})
    if user is None:
        raise "TEST"
    return user
