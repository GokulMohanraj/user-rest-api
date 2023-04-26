import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="pass123",
    database="user_details")
print(mydb)
my_cursor = mydb.cursor(dictionary=True)
