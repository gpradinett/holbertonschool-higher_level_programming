#!/usr/bin/python3
"""
script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
"""
from requests import post
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) < 2:
        q = {'q': ''}
    else:
        q = {'q': sys.argv[1]}
    try:
        response = post(url, q).json()
    except ValueError:
        print("Not a valid JSON")
    if response == {}:
        print("No result")
    else:
        print("[{}] {}".format(response.get('id'), response.get('name')))
