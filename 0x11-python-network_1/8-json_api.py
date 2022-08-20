#!/usr/bin/python3
"""
script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
https://www.geeksforgeeks.org/response-json-python-requests/
"""
if __name__ == "__main__":
    import requests
    from sys import argv  # for command line arguments

    url = "http://0.0.0.0:5000/search_user"
    # Setear letter como el comando de linea si pasaron uno y sino como ""
    if len(argv) > 1:
        letter = argv[1]  # letter to be sent as a command line argument
    else:
        letter = ""

    # Set value to send
    values = {'q': letter}
    # Post method with requests
    response = requests.post(url, values)
    # Igual json a la respuesta si existe
    try:
        json = response.json()
        if json:
            print("[{}] {}".format(json["id"], json["name"]))
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
