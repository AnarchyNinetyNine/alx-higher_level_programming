#!/usr/bin/python3

"""
    This module fetches the status from a specified URL using urllib.
    The response body is displayed in a formatted manner.
"""


import urllib.request


def fetch_status(url):

    """
        Fetches the status of a given URL.

        Args:
            url (str): The URL to fetch.

        Returns:
            None
    """

    with urllib.request.urlopen(url) as response:
        body = response.read()

    print("Body response:")
    print("\t- type:", type(body))
    print("\t- content:", body)
    print("\t- utf8 content:", body.decode('utf-8'))

if __name__ == "__main__":
    fetch_status('https://alx-intranet.hbtn.io/status')
