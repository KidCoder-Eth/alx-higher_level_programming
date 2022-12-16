#!/usr/bin/python3

"""
Lists 10 commits sorted from the recent to the oldest in the repository
rails by the user rails
"""

import requests
from sys import argv

if __name__ == "__main__":
    github_commits = 'https://api.github.com/repos/'\
                     + argv[2] + '/' + argv[1] + '/commits'
    req = requests.get(github_commits)
    if "json" not in req.headers.get('content-type'):
        print("Not a valid JSON")
    else:
        res = req.json()
        i = 0
        for r in res:
            if i > 9:
                break
            print(r.get('sha') + ': ', end="")
            print(r.get('commit').get('author').get('name'))
            i += 1
