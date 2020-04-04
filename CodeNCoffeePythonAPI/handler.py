import json
import random


def hello(event, context):
    body = {
        "message": "Hello Code and Coffee Friends",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """

def coffeeOfTheDay(event, context):
    # create a list of coffees
    coffees = [ "dark roast",
                "medium roast",
                "light roast",
                "kona",
                "java",
                "decaf" ]

    # pick a random number from the indexes in the array
    coffeeIdx = random.randint(0, len(coffees) -1)

    # get query string parameters for the name or default it
    try:
        yourName = event["queryStringParameters"]["name"]
    except:
        yourName = "Code and Coffee"

    # build the message
    yourMessage = f"Hello {yourName}, Your coffee of the day is {coffees[coffeeIdx]}"

    # create the body with the random coffee
    body = {
        "message": yourMessage
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

