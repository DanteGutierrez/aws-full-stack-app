
# NOTE: who can update books? Are we using this endpoint for checking out books?
def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }