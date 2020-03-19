import os
import pymysql

# Get username from Cloud9 workspace
# modify this variable if running on another environment
username = os.getenv('C9_USER')

# Conntect to the Database
connection = pymysql.connect(
    host='localhost',
    user=username,
    password="",
    db="Chinook"
)

try:
    # Run a query
    with connection.cursor() as cursor:
        sql = "select * from Artist;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    # Close the connection, regardless of weather the above was successful
    connection.close()
