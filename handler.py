import json
from botocore.vendored import requests


def hello(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    print(event)

    r = requests.post('XXX/api/1/iot/medication', json=event)

    response = {
        "statusCode": 200,
        "req": json.dumps(body),
        "res": json.dumps(r)
    }

    return response

