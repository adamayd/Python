import json

def squaredNum(event, context):
    yourNum = event["queryStringParameters"]["number"]

    yourSquaredNum = float(yourNum) ** 2

    body = {
        "message": "Here is the squared value of the number you inserted",
        "yourNumber": yourSquaredNum
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

def hello(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

def shopping(event, context):
    yourItem = event["queryStringParameters"]["item"]

    body = {
        "message": "Next time you go to the store you need the following item",
        "yourItem": yourItem
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
