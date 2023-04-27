# Flask RESTful API

This is a Flask RESTful API that allows you to perform CRUD (Create, Read, Update, Delete) operations on a MySQL database. 

## Prerequisites

- Python 3.6 or higher
- Flask 
- Flask RESTful
- MySQL Connector Python

## Installation

1. Clone the repository
2. Install dependencies with `pip install -r requirements.txt`
3. Create a MySQL database and configure the `connection.py` file with your database information
4. Run the app with `python server.py`

# API Endpoints

The following endpoints are available:

## 1) GET /users

This endpoint returns a list of all users objects in the database in JSON format.

##### Example:
```
http://localhost:5000/users
```


## 2) GET /user/<user_id>

This endpoint returns the user with the specified `user_id`.
Input: 
    <user_id> : User ID

    Output:
    Response code: 200
    Return the user object in JSON format for the given user id
    Eg: 
    {
        'user_id': '1',
        'username': 'jack',
        'number': '5797675345',
        'email': 'xyz@gmail.com'
    }

    Response code: 404
    If the given user id doesnt exist, the API will return 404 error.
    Return error message
    {
        'message': 'user_id doesnt exist'
    }

##### Example:
```
http://localhost:5000/user/1
```

## 3) POST /user

This endpoint allows you to add a new user to the database.

Input:
    {
        'user_id': '3',
        'username': 'johndoe',
        'number': '1234567890',
        'email': 'johndoe@example.com'
    }


##### Example:
```
POST http://localhost:5000/user
```

## 4) PUT /user/{user_id}

This endpoint allows you to update the user with the specified `user_id`.

Data:
{
    "number": 9876543210
}

##### Example:
```
PUT http://localhost:5000/user/3
```

## 5) DELETE /user/{user_id}

This endpoint allows you to delete the user with the specified `user_id`.

Input
    <user_id> = user ID
     Output:
    Response code: 200
        {
            'message': 'User-ID Deleted'
        }

    Response code: 404
    If the given user id doesnt exist, the API will return 404 error.
    Return error message
    {
        'message': 'user_id doesnt exist'
    }


##### Example:
```
DELETE http://localhost:5000/user/3
```

