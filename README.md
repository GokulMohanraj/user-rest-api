# user-rest-api

This service implements a User REST API. 
It provides API endpoing for adding, modify and delete users thru REST APIs.

It uses Flask and Flask-Restful libraries.

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
