#!/usr/bin/python3
"""
Returns an object (Python data structure)
represented by a JSON string.
metodo: loads() del modulo json de python.
"""
import json


def from_json_string(my_str):
    """
    Convert JSON object to a Python object.
    """
    return json.loads(my_str)
