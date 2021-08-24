import boto3

dynamoDB = boto3.client('dynamodb')


def get_crew_profile_handler(event: dict, context):
    user_id = event.get('User_ID')
    crew_id = event.get('Crew_ID')
    if crew_id is not None:
        response = dynamoDB.get_item(
            Key={
                'User_ID': {
                    'S': user_id,
                },
                'Crew_ID': {
                    'S': crew_id,
                },
            },
            TableName='crew'
        )
    else:
        response = dynamoDB.query(
            TableName='crew',
            KeyConditionExpression='User_ID = :user_id',
            ExpressionAttributeValues={
                ":user_id": {"S": user_id}
            }

        )

    response['statusCode'] = 200
    return response
