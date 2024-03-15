# Importing MySQL Connector/Python 
import mysql.connector as connector
from mysql.connector import Error

# Import MySQLConnectionPool class
from mysql.connector.pooling import MySQLConnectionPool

try:
    connection=connector.connect(user="root",password="")
except Error as er:
    print(er.msg)


dbconfig={"database":"little_lemon_db", "user":"root", "password":""}
try:
    pool = MySQLConnectionPool(pool_name="pool_a", pool_size=2, host='localhost', **dbconfig)
    print("The connection pool is created with name:", pool.pool_name)
    print("The pool size is:", pool.pool_size)
except Error as err:
    print("Error Code:", err.errno)
    print("Error Message:", err.msg)

#Obtaining connection 
print("Getting a connection from the pool.")

connection = pool.get_connection()
if connection.is_connected():
    cursor = connection.cursor()

print("'connection' object is created with a connection from the pool")