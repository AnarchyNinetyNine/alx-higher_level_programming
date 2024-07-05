#!/usr/bin/python3

"""
    This module fetches the value of the 'X-Request-Id' header
    from a specified URL using urllib.
"""


import urllib.request
import sys


def fetch_request_id(url):

    """
        Fetches the 'X-Request-Id' header from the given URL.

        Args:
            url (str): The URL to fetch.

        Returns:
            None
    """

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(response.info()['X-Request-Id'])


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./0-hbtn_status.py <URL>")
    else:
        fetch_request_id(sys.argv[1])
