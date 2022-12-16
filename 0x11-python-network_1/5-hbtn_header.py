#!/usr/bin/python3

"""
This will takes a URL then will send a request and display
the value of the X-Request-Id found in the header
"""

import requests
from sys import argv

if __name__ == "__main__":
    response = requests.get(argv[1])
    print(response.headers.get('x-request-id'))
