from models.response import response

# NOTE: who can get users?
def lambda_handler(event, context):

    if "pathParameters" not in event or "queryStringParameters" not in event:
        return response(400, {"message":"missing request data"})
    
    path = event["pathParameters"]

    if path is not None and "id" in path:
        # TODO get by id
        return response(0, {})
    
    params = event["queryStringParameters"]

    # Full collection here

    if params is not None and "name" in params:
        # TODO filter by name
    if params is not None and "role" in params:
        # TODO filter by role

    # TODO implement
    return response(0, {})
