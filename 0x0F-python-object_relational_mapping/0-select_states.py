#!/usr/bin/python3

"""
    Script to retrieve and print all states from a MySQL database.

    Usage:
        ./0-select_states.py username password database_name

    Args:
        username (str): MySQL username for authentication.
        password (str): MySQL password for authentication.
        database_name (str): Name of the MySQL database to connect to.

    This script connects to a MySQL server running on localhost at port 3306,
    retrieves all states from the specified database
    sorted by id in ascending order, and prints each state
    in the format (id, 'name').
"""


import sys
import MySQLdb


def main():

    """ Main function to execute the script. """

    # Check if the correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: ./0-select_states.py username password database_name")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    # Connect to MySQL server
    try:
        db = MySQLdb.connect(host="localhost",
                             user=username,
                             passwd=password,
                             db=database_name,
                             port=3306)
        cursor = db.cursor()

        # Execute the query to select all states sorted by id
        cursor.execute("SELECT * FROM states ORDER BY id ASC")
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
    main()
