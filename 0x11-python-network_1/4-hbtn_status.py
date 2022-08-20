#!/usr/bin/python3
# Python script fetches https://intranet.hbtn.io/status
# https://www.geeksforgeeks.org/python-requests-tutorial/

if __name__ == "__main__":
    import requests

    url = "https://intranet.hbtn.io/status"
    data_req = requests.get(url)

    print("Body response:\n\t- type: {}\n\t- content: {}"
          .format(type(data_req.text), data_req.text))
