#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status
"""
if __name__ == "__main__":
    import urllib.request

    url = "https://intranet.hbtn.io/status"
    request = urllib.request.Request(url)

    with urllib.request.urlopen(request) as response:
        content = response.read()
        print("Body response:")
        print("\t- type:", type(content))
        print("\t- content:", content)
        print("\t- utf8 content:", content.decode("utf-8"))
