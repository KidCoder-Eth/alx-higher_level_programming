#!/usr/bin/python3

"""
This will takes a URL with an email and then will send a POST request
as a parameter. Then will display the body of the response
"""

import urllib.request
from sys import argv

if __name__ == "__main__":
    info = urllib.parse.urlencode({'email': argv[2]})
    info = info.encode('ascii')
    with urllib.request.urlopen(argv[1], info) as f:
        print(f.read().decode('utf-8'))
