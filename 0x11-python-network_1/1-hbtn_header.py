#!/usr/bin/python3

"""
This will takes a URL and then will send a request and display the value of the
X-Request-Id
"""

import urllib.request
from sys import argv

if __name__ == "__main__":
    with urllib.request.urlopen(argv[1]) as f:
        print(f.headers.get('X-Request-Id'))
