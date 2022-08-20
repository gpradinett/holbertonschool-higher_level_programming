#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the
URL and displays the value of the X-Request-Id var
iable found in the header of the response
"""
if __name__ == "__main__":
    import urllib.request
    import sys

    url = sys.argv[1]
    data = urllib.request.Request(url)

    with urllib.request.urlopen(data) as response:
        content = response.headers.get("X-Request-Id")
        print(content)
