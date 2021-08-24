def lambda_handler(event, context):
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
    response = {}
    if not bool(event["body"]["FirstName"]["S"]):
        response["FirstNameError"] = "First name cannot be empty"
    if not bool(event["body"]["LastName"]["S"]):
        response["LastNameError"] = "Last name cannot be empty"
    if not bool(event["body"]["Nickname"]["S"]):
        response["NicknameError"] = "Nickname cannot be empty"

    if bool(response):
        response["hasError"] = True
    else:
        response["hasError"] = False
    return response
