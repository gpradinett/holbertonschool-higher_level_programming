#!/usr/bin/python3
"""
Appends a string at the end of a text file.
"""


def append_write(filename="", text=""):
    """
    method that adds text to a file
    """
    with open(filename, 'a', encoding="utf8-") as f:
        return f.write(text)
