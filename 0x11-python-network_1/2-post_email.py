#!/usr/bin/python3

"""
    This module takes in a URL and an email, sends a POST request
    to the passed URL with the email as a parameter, and displays
    the body of the response (decoded in utf-8).
"""


import sys
import urllib.request
import urllib.parse


# Get the URL and email from command-line arguments
url = sys.argv[1]
params = {'email': sys.argv[2]}

# Encode the parameters for the POST request
data = urllib.parse.urlencode(params).encode('utf-8')

# Create the request object with the URL and encoded data
request = urllib.request.Request(url, data)

# Send the request and read the response
with urllib.request.urlopen(request) as response:
    print(response.read().decode('utf-8'))
