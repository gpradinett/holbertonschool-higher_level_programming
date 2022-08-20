#!/usr/bin/python3
"""
gets the status code to the passed URL
"""

from requests import get
import sys

if __name__ == "__main__":
    resp = get(sys.argv[1])
    if (resp.status_code >= 400):
        print("Error code: {}".format(resp.status_code))
    else:
        print("{}".format(resp.content.decode('utf-8')))
