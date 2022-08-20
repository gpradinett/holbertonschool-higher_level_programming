#!/usr/bin/python3
# Python script fetches https://intranet.hbtn.io/status
# https://www.geeksforgeeks.org/python-requests-tutorial/

if __name__ == "__main__":
    import requests

    req = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type:", type(req.text))
    print("\t- content:", req.text)
