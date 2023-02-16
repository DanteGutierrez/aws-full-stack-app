from bson import json_util


def response(code, body):
    return {
        "statusCode": code,
        "headers": {"Content-Type": "application/json"},
        "body": json_util.dumps(body, default=str),
    }
