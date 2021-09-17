# Title: pysports_queries.py
# Author: Tara Botts
# Date: September 12, 2021
# Description: Assignment 8.3

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
    cursor = db.cursor()

    #Select query from the team table 
    cursor.execute("SELECT team_id, team_name, mascot FROM team")

    #Display results from query 
    teams = cursor.fetchall()
    print("\n  -- DISPLAYING TEAM RECORDS --")
    
    #Using a for loop to iterate over the cursor 
    for team in teams: 
        print("  Team ID: {}\n  Team Name: {}\n  Mascot: {}\n".format(team[0], team[1], team[2]))

    #Select query from the player table 
    cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")

    #Display results from query
    players = cursor.fetchall()
    print ("\n  -- DISPLAYING PLAYER RECORDS --")

    #Using a for loop to iterate over the cursor
    for player in players:
        print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team ID: {}\n".format(player[0], player[1], player[2], player[3]))

    input("\n\n  Press any key to continue... ")

#Display if error
except mysql.connector.Error as err:

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

#Closes MySQL connection
finally:
    db.close()