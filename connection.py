import mysql.connector

# The username and password for the database
# TODO: To move the DB details to config file

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="pass123",
    database="user_details")
print(mydb)
my_cursor = mydb.cursor(dictionary=True)
