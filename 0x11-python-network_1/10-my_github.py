#!/usr/bin/python3

"""
This will takes your Github accout credentials and uses the
Github API in order to display your id
"""

import requests
from sys import argv

if __name__ == "__main__":
    r = requests.get('https://api.github.com/user', auth=(argv[1], argv[2]))
    if "json" not in r.headers.get('content-type'):
        print("Not a valid JSON")
    else:
        res = r.json()
        print(res.get('id'))
