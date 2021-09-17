# Title: mysql_test.py
# Author: Tara Botts
# Date: September 12, 2021
# Description: Assignment 8.2

#Import statements
import mysql.connector
from mysql.connector import errorcode

#Database config object
config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "localhost",
    "database": "pysports",
    "raise_on_warnings": True
}

#Connection test code
try:
    #Connect to pysports database 
    db = mysql.connector.connect(**config)
    
    # Display connection status 
    print("\n  Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    input("\n\n  Press any key to continue...")

except mysql.connector.Error as err:
#Display if error

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    #Closes MySQL connection
    db.close()