#!/usr/bin/python3
"""
script that takes your GitHub credentials (username and password) and uses the GitHub APIto display your id
https://blog.devgenius.io/how-to-use-api-request-in-python-6ef370f9f771
"""

from requests import get
from requests.auth import HTTPBasicAuth
import sys

if __name__ == "__main__":
    user = sys.argv[1] # se guarda el usuario pasado como primer comando en linea
    passwd = sys.argv[2] # guardamos la contr que se pase como 2 comand en linea
    url = "https://api.github.com/user"
    # Se hace una request usando autentificacion
    response = get(url, auth=HTTPBasicAuth(user, passwd)).json()
    print(response.get('id'))
