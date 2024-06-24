#!/usr/bin/python3

"""
    Script to retrieve and print states from a MySQL database
    starting with 'N'.

    Usage:
        ./1-filter_states.py username password database_name

    Args:
        username (str): MySQL username for authentication.
        password (str): MySQL password for authentication.
        database_name (str): Name of the MySQL database to connect to.

    This script connects to a MySQL server running on localhost at port 3306,
    retrieves states whose names start with 'N' from the specified database,
    and prints each state in the format (id, 'name')
    sorted by id in ascending order.
"""


import sys
import MySQLdb


def filter_states(username, password, database_name):

    """
        Function to connect to MySQL server and retrieve
        states starting with 'N'.

        Args:
            username (str): MySQL username for authentication.
            password (str): MySQL password for authentication.
            database_name (str): Name of the MySQL database to connect to.
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

        # Execute the query to select states starting with 'N'
        cursor.execute(
                "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
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
    if len(sys.argv) != 4:
        print("Usage: ./1-filter_states.py username password database_name")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    filter_states(username, password, database_name)
