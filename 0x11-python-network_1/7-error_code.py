#!/usr/bin/python3

"""
This will takes a URL then will send a request and display the body of
the response
"""

import requests
from sys import argv

if __name__ == "__main__":
    r = requests.get(argv[1])
    status = r.status_code
    if status >= 400:
        print("Error code: " + str(status))
    else:
        print(r.text)
