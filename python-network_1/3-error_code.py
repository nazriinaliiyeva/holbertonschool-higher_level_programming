#!/usr/bin/python3
"""
Fetches a URL and displays the body of the response.
Handles HTTPError exceptions.
"""

import sys
from urllib import request, error

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with request.urlopen(url) as response:
            body = response.read()
            print(body.decode("utf-8"))
    except error.HTTPError as e:
        print(f"Error code: {e.code}")
