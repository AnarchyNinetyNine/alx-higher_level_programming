#!/usr/bin/python3

"""
    This module takes GitHub credentials (username and personal access token)
    and uses the GitHub API to display the user's id.
"""


import sys
import requests


if __name__ == "__main__":

    # Get username and personal access token from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]

    # GitHub API endpoint for authenticated user
    url = f"https://api.github.com/user"

    # Set up Basic Authentication using personal access token as password
    auth = (username, password)

    # Send GET request to GitHub API
    response = requests.get(url, auth=auth)

    # Check if request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        user_data = response.json()
        # Display the user's id
        print(user_data['id'])
    else:
        # If request failed, print None
        print(None)
