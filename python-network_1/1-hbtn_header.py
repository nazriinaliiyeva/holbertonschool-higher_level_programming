#!/usr/bin/python3
"""documentation"""


import sys
from urllib import request

if __name__ == "__main__":
    url = sys.argv[1]
    with request.urlopen(url) as response:
        x_request_id = response.getheader("X-Request-Id")
        if x_request_id is not None:
            print(x_request_id)
