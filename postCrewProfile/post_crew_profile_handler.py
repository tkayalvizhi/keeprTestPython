import boto3

dynamoDB = boto3.client('dynamodb')


def handler(event: dict, context: dict):
    """*first_name_error = ""
    last_name_error = ""
    nickname_error = ""
    has_error = False
    if event["FirstName"] is None or event["LastName"] is None or event["Nickname"] is None:
        has_error = True
        first_name_error = "First name cannot be empty \n"
    if event """
    error_message = {}

    if event["FirstName"] is None:
        error_message["FirstName"] = "First name cannot be empty"
    if event["LastName"] is None:
        error_message["LastName"] = "Last name cannot be empty"
    if event["Nickname"] is None:
        error_message["Nickname"] = "Nickname cannot be empty"

    response: dict = dynamoDB.put_item(
        TableName="crew",
        Item=event,
        ReturnValues='UPDATED_NEW'
    )

    dynamoDB.put_item(
        TableName="crewError",
        Item={
            "User_ID": event["User_ID"],
            "Crew_ID": event["Crew_ID"],
            # "hasError": {"S": response["statusCode"]},
            "error": {"M": str(response['ResponseMetadata']['HTTPStatusCode'])}
        }
    )

    return response
