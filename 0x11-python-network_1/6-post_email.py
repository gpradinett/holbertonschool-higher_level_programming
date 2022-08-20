#!/usr/bin/python3
"""
sends a POST request to the passed URL
recurso: https://www.geeksforgeeks.org/post-method-python-requests/
"""
from requests import post
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = {'email': sys.argv[2]}
    response = post(url, email).content.decode('utf-8')
    print(response)
