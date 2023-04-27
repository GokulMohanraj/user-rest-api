# Import necessary libraries
from flask import Flask
from flask_restful import Resource, Api, reqparse, abort
from connection import mydb, my_cursor  # Importing database connection and cursor from a separate file

# Initialize Flask app and API
app = Flask(__name__)
api = Api(app)

# Define arguments for parsing request data
post_args = reqparse.RequestParser()
post_args.add_argument('user_id', type=int, help='user_id is not empty', required=True)
post_args.add_argument('username', type=str, help='username is not empty', required=True)
post_args.add_argument('number', type=int, help='number is not empty', required=True)
post_args.add_argument('email', type=str, help='email is not empty', required=True)

put_args = reqparse.RequestParser()
put_args.add_argument('username', type=str)
put_args.add_argument('number', type=int)
put_args.add_argument('email', type=str)


# Define resource classes
class Data(Resource):
    # Define GET method to retrieve all users data
    try:
        def get(self):
            query = 'SELECT * FROM user_table'
            my_cursor.execute(query)
            result = my_cursor.fetchall()
            return result
    except Exception as e:
        return e
class User(Resource):
    # Define GET method to retrieve user data by user_id
    try:
        def get(self, user_id):
            query = 'SELECT * FROM user_table WHERE user_id = %s'
            values = (user_id,)
            my_cursor.execute(query, values)
            result = my_cursor.fetchone()
            if result:
                return result
            else:
                return {'message': 'User not found'}, 404
    except Exception as e:
        return e
class post(Resource):
    # Define POST method to add new user data
    try:
        def post(self):
            args = post_args.parse_args()
            user_id = args['user_id']
            query = 'SELECT user_id FROM user_table WHERE user_id = %s'
            values = [user_id]
            my_cursor.execute(query, values)
            if my_cursor.fetchone():
                return{'message': 'User_id is already exist'},404
            else:
                try:
                    query = 'INSERT INTO user_table (user_id, username, number, email) VALUES (%s, %s, %s, %s)'
                    values = (user_id, args['username'], args['number'], args['email'])
                    my_cursor.execute(query, values)
                    mydb.commit()
                    return {'message': 'New user inserted'}
                except Exception as e:
                    mydb.rollback()
                    return {'message': str(e)}, 500
    except Exception as e:
        return e
class put(Resource):
    # Define PUT method to update user data by user_id
    try:
        def put(self, user_id):
            query = 'SELECT * FROM user_table WHERE user_id = %s'
            values = (user_id,)
            my_cursor.execute(query, values)
            result = my_cursor.fetchone()
            if result:
                args = put_args.parse_args()
                query = 'UPDATE user_table SET'
                values = []
                if args['number']:
                    query += ' number = %s,'
                    values.append(args['number'])
                if args['email']:
                    query += ' email = %s,'
                    values.append(args['email'])
                if not values:
                    return {'message': 'No data provided for update'}, 400

                query = query[:-1] + ' WHERE user_id = %s'
                values.extend([user_id])
                try:
                    my_cursor.execute(query, tuple(values))
                    mydb.commit()
                    return {'message': 'Updated sucessfully'}
                except Exception as e:
                    mydb.rollback()
                    return {'message': str(e)}, 500
            else:
                return {'message': 'User not found'}, 404
    except Exception as e:
        return e

class delete(Resource):
    # Define DELETE method to delete user data by user_id
    try:
        def delete(self, user_id):
            query = 'SELECT user_id FROM user_table WHERE user_id = %s'
            values = [user_id]
            my_cursor.execute(query, values)
            if not my_cursor.fetchone():
                return{'message': 'There is no such user_id'},404
            else:
                query = 'DELETE FROM user_table WHERE user_id = %s'
                values = (user_id,)
                try:
                    my_cursor.execute(query, values)
                    mydb.commit()
                    return {'message': 'User deleted successfully'}
                except Exception as e:
                    mydb.rollback()
                    return {'message': str(e)}, 500
    except Exception as e:
        return e

api.add_resource(Data, '/users')
api.add_resource(User, '/user/<int:user_id>')
api.add_resource(post, '/user')
api.add_resource(put, '/user/<int:user_id>')
api.add_resource(delete, '/user/<int:user_id>')


if __name__ == '__main__':
    app.run(debug=True)
