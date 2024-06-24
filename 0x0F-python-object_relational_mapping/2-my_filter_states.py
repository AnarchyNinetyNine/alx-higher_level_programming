#!/usr/bin/python3

"""
    Script to filter and display states from a MySQL database
    based on a given state name.

    Usage:
        ./2-my_filter_states.py username password database_name state_name
"""


import sys
import MySQLdb


def filter_states(username, password, database_name, state_name):

    """
    Function to connect to MySQL server and filter states
    based on state_name.

    Args:
        username (str): MySQL username for authentication.
        password (str): MySQL password for authentication.
        database_name (str): Name of the MySQL database to connect to.
        state_name (str): Name of the state to search
        for in the states table.
    """
    try:
        # Connect to MySQL server
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database_name
        )

        cursor = db.cursor()

        # Execute the query to select states based on state_name
        query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
        cursor.execute(query, (state_name,))
        states = cursor.fetchall()

        # Print each state in the format (id, 'name')
        for state in states:
            print(state)

        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print(f"MySQL Error {e.args[0]}: {e.args[1]}")
        sys.exit(1)


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    filter_states(username, password, database_name, state_name)
