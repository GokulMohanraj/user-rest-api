# user-rest-api

API
# 1)    GET /users

    Returns list of user objects in JSON format


# 2)    GET /user:<user_id>

    Returns the user details for the give user id.
    Input: 
    <user_id> : User ID

    Output:
    Response code: 200
    Return the user object in JSON format for the given user id
    Eg: 
    {

    }

    Response code: 404
    If the given user id doesnt exist, the API will return 404 error.
