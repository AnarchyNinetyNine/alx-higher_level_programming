#!/usr/bin/python3

"""
    This module takes in a URL, sends a request to the URL, and displays
    the value of the variable X-Request-Id in the response header.
"""


import sys
import requests


if __name__ == "__main__":

    # Get the URL from command-line arguments
    url = sys.argv[1]

    # Send the request
    response = requests.get(url)

    # Get the value of the 'X-Request-Id' header
    x_request_id = response.headers.get('X-Request-Id')

    # Print the value of 'X-Request-Id'
    print(x_request_id)
