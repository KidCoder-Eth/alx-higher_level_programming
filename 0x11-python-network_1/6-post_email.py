#!/usr/bin/python3

"""
This will take a URL with an email and then will send a POST request with the
emails parameter.Then will display the body of the response
"""

import requests
from sys import argv

if __name__ == "__main__":
    r = requests.post(argv[1], data={'email': argv[2]})
    print(r.text)
