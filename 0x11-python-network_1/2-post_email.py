#!/usr/bin/python3

import sys
import urllib.request
import urllib.parse


url = sys.argv[1]
params = {}
params['email'] = sys.argv[2]

data = data = urllib.parse.urlencode(params).encode('utf-8')
request = urllib.request.Request(url, data)
with urllib.request.urlopen(request) as response:
    print(response.read().decode('utf8'))
