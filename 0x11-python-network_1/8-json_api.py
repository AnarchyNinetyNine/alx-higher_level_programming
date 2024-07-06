#!/usr/bin/python3

"""
    This module takes in a letter, sends a POST request to
    http://0.0.0.0:5000/search_user with the letter as a parameter,
    and displays the response based on the JSON format and content.
"""


import sys
import requests


if __name__ == "__main__":

    # Get the letter from command-line arguments or set default to ""
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""

    # URL and payload
    url = 'http://0.0.0.0:5000/search_user'
    payload = {'q': q}

    # Send the POST request
    response = requests.post(url, data=payload)

    try:
        # Try to parse the JSON response
        json_response = response.json()

        # Check if JSON is empty
        if json_response:
            print("[{}] {}".format(json_response['id'], json_response['name']))
        else:
            print("No result")

    except ValueError:
        # Invalid JSON
        print("Not a valid JSON")
