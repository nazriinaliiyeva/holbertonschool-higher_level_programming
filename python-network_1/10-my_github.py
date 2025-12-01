#!/usr/bin/python3
"""
Takes your GitHub credentials and uses the GitHub API to display your id
"""

import sys
import requests


if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]

    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, token))

    try:
        user_data = response.json()
        print(user_data.get("id"))
    except ValueError:
        print(None)
