#!/usr/bin/python3
"""documentation"""

import sys
import requests

if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    response = requests.post(
            "http://0.0.0.0:5000/search_user", data={"q": letter}
    )

    try:
        result = response.json()
        if result:
            print(f"[{result.get('id')}] {result.get('name')}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
