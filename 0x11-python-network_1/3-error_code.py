#!/usr/bin/python3
"""
Python script that takes in a URL,
sends a request
to the URL and displays the body
of the response
(decoded in utf-8).
"""

if __name__ == "__main__":
    import sys
    import urllib.request

    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            content = response.read()
            print(content.decode())
    except URLError as err:
        print("Error code:", err.code)
