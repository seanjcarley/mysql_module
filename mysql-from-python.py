import os
import pymysql
import datetime

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
    '''with connection.cursor() as cursor:
        sql = "select * from Artist;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        sql = 'select * from Genre;'
        cursor.execute(sql)
        for row in cursor:
            print(row)'''
    with connection.cursor() as cursor:
        cursor.execute ("""CREATE TABLE IF NOT EXISTS
                        Friends(name char(20), age int, DOB datetime);""")
        # Note that the above will still display a warning (not error) if the
        # table already exists
finally:
    # Close the connection, regardless of weather the above was successful
    connection.close()
