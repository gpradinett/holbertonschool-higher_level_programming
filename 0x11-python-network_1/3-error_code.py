#!/usr/bin/python3
"""
Python script that takes in a URL,
sends a request
to the URL and displays the body
of the response
(decoded in utf-8).
"""

if __name__ == "__main__":
    import urllib.request
    from sys import argv

    url = urllib.request.Request(argv[1])
    try:
        with request.urlopen(url) as html:
            html = html.read()
            print("{}".format(html.decode('utf-8')))
    except error.URLError as err:
        print("Error code: {}".format(err.code))
