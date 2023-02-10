from models.response import response

# NOTE: only admins can delete books
def lambda_handler(event, context):

    if "pathParameters" not in event:
        return response(400, {"message":"need to select id"})
    
    params = event["pathParameters"]

    if params is None or "id" not in params:
        return response(400, {"message":"needs id"})
    
    # TODO get book by id

    # if book is None:
    #   return response(404, {"message":"entry not found"})

    # TODO delete
    return response(200, {})
