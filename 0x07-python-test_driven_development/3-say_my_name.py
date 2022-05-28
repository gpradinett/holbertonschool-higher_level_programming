#!/usr/bin/python3
"""
Python function that prints my name is first name and last name
"""


def say_my_name(first_name, last_name=""):
    """
    Print string: first name and last name
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
