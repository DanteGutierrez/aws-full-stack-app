from models.response import response

# NOTE: users can checkout books
def lambda_handler(event, context):
    # TODO implement
    return response(200, {"message": "Hello from Lambda!"})


print(lambda_handler({}, None))
