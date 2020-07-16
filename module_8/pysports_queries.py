""" 
    Title: pysports_queries.py
    Author: Professor Krasso
    Date: 15 July 2020
    Description: Test program for executing queries against the pysports database. 
"""

""" import statements """
import mysql.connector
from mysql.connector import errorcode

""" database config object """
config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

try:
    """ try/catch block for handling potential MySQL database errors """ 

    db = mysql.connector.connect(**config) # connect to the pysports database 

    cursor = db.cursor()

    # select query from the team table 
    cursor.execute("SELECT team_id, team_name, mascot FROM team")

    # get the results from the cursor object 
    teams = cursor.fetchall()

    print("\n  -- DISPLAYING TEAM RECORDS --")
    
    # iterate over the teams data set and display the results 
    for team in teams: 
        print("  Team ID: {}\n  Team Name: {}\n  Mascot: {}\n".format(team[0], team[1], team[2]))

    # select query for the player table 
    cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")

    # get the results from the cursor object 
    players = cursor.fetchall()

    print ("\n  -- DISPLAYING PLAYER RECORDS --")

    # iterate over the players data set and display the results
    for player in players:
        print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team ID: {}\n".format(player[0], player[1], player[2], player[3]))

    input("\n\n  Press any key to continue... ")

except mysql.connector.Error as err:
    """ handle errors """

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    """ close the connection to MySQL """
    
    db.close()