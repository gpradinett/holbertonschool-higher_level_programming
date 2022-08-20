#!/usr/bin/python3
"""Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email
as a parameter, and displays the body of the response(decoded in utf-8)
"""

if __name__ == "__main__":
    import sys
    from urllib import parse, request

    url = sys.argv[1]
    email = {"email": sys.argv[2]}
    email = parse.urlencode(email).encode('ascii')
    with request.urlopen(url, email) as response:
        print(response.read().decode('utf-8'))
