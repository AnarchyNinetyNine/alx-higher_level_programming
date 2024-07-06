#!/usr/bin/python3

"""
    This module takes in a URL, sends a request to the URL, and displays
    the body of the response (decoded in utf-8). It handles HTTP errors
    by printing the error code.
"""


import sys
import urllib.request
import urllib.error


if __name__ == "__main__":
    # Get the URL from command-line arguments
    url = sys.argv[1]

    try:
        # Send the request and read the response
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        # Print the error code if an HTTP error occurs
        print("Error code:", e.code)
