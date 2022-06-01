#!/usr/bin/python3
"""
Function that returns the JSON representation of an object (string)
Vamos a usar el modulo json de python y vamos a usar el methodo:
dumps() para convertir un objeto de python a un objeto de JSON.
"""
import json


def to_json_string(my_obj):
    """
    Returns th JSON representation of my_obj.
    """
    return json.dumps(my_obj)
