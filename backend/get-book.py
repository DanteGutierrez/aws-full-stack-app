from models.response import response

# NOTE: users and admins can get books
def lambda_handler(event, context):

    if "pathParameters" not in event or "queryStringParameters" not in event:
        return response(400, {"message":"missing request data"})
    
    path = event["pathParameters"]

    if path is not None and "id" in path:
        # TODO get by id
        return response(0, {})
    
    params = event["queryStringParameters"]

    # Full collection here

    if params is not None and "title" in params:
        # TODO filter by title
    if params is not None and "author" in params:
        # TODO filter by author
    if params is not None and "genre" in params:
        # TODO filter by genre
    if params is not None and "purchase_price" in params:
        # TODO filter by purchase_price
    if params is not None and "rent_price" in params:
        # TODO filter by rent_price
    if params is not None and "condition" in params:
        # TODO filter by condition
    if params is not None and "is_paperback" in params:
        # TODO filter by is_paperback
    if params is not None and "is_available" in params:
        # TODO filter by is_available

    # TODO return collection
    return response(0, {})
