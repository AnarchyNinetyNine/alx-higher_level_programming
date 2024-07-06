#!/usr/bin/python3

"""
    This module fetches https://alx-intranet.hbtn.io/status
    using the requests package and displays the body of the response.
"""


import requests


if __name__ == "__main__":

    # Fetch the URL
    response = requests.get('https://alx-intranet.hbtn.io/status')

    # Get the content of the response
    content = response.text

    print("Body response:")
    print("\t- type:", type(content))
    print("\t- content:", content)
