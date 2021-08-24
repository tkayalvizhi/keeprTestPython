import boto3

dynamoDB = boto3.client('dynamodb')


def handler(event: dict, context: dict):
    """event is of type dict
    eg:
    {
    "User_ID" : "testUser@keepr.com",
    "body" : {
    "FirstName": { "S" : "Harry"},
    "LastName": { "S" : "Potter"},
    "MiddleName": { "S" : "James"},
    "Nickname": { "S" : "Harry"}
    }
    }"""

    item = {"User_ID": {"S": event["User_ID"]},
            "Crew_ID": {"S": event["body"]["FirstName"]["S"] + event["body"]["LastName"]["S"]}}

    for field in event["body"].keys():
        item[field] = event["body"][field]

    response = dynamoDB.put_item(
        TableName="crew",
        Item=item,
        ReturnValues='UPDATED_NEW'
    )

    return response
