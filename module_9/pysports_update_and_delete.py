# Title: pysports_update_and_delete.py
# Author: Tara Botts
# Date: September 19, 2021
# Description: Assignment 9.3

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

def show_players(cursor, title):

    #Select inner join query from the player table 
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

    #Display results from query
    players = cursor.fetchall()

    print("\n  -- {} --".format(title))
    
    #Using a for loop to iterate over the cursor
    for player in players:
        print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team Name: {}\n".format(player[0], player[1], player[2], player[3]))

#Connection test code
try:
    #Connect to pysports database 
    db = mysql.connector.connect(**config)
    cursor = db.cursor()
       
    #Insert a new player 
    add_player = ("INSERT INTO player(first_name, last_name, team_id)"
                 "VALUES(%s, %s, %s)")

    #New player data 
    player_data = ("Smeagol", "Shire Folk", 1)

    #Insert new player record
    cursor.execute(add_player, player_data)

    #Commit the insert to the pysports database 
    db.commit()

    #Display records in player table after insert
    show_players(cursor, "DISPLAYING PLAYERS AFTER INSERT")

    #Update the new player's data 
    update_player = ("UPDATE player SET team_id = 2, first_name = 'Gollum', last_name = 'Ring Stealer' WHERE first_name = 'Smeagol'")

    #Execute the updated data
    cursor.execute(update_player)

    #Display records in player table after update 
    show_players(cursor, "DISPLAYING PLAYERS AFTER UPDATE")

    #Delete the player we inserted and updated 
    delete_player = ("DELETE FROM player WHERE first_name = 'Gollum'")

    #Execute the deletion
    cursor.execute(delete_player)

    #Display records in player table after deletion
    show_players(cursor, "DISPLAYING PLAYERS AFTER DELETE")

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