#!/usr/bin/python3

"""
    This module takes in a URL, sends a request to the URL, and displays
    the body of the response. If the HTTP status code is greater than or
    equal to 400, it prints an error message with the status code.
"""


import sys
import requests


if __name__ == "__main__":

    # Get the URL from command-line arguments
    url = sys.argv[1]

    # Send the GET request
    response = requests.get(url)

    # Check the status code
    if response.status_code >= 400:
        print("Error code:", response.status_code)
    else:
        print(response.text)
