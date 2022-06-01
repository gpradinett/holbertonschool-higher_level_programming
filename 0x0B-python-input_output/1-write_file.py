#!/usr/bin/python3
"""
Writes in a text file.
"""


def write_file(filename="", text=""):
    """
    Function that writes to a text file
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
