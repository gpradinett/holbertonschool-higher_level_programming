#!/usr/bin/python3
"""
Reads from a file and prints.
"""


def read_file(filename=""):
    """
    Reads from filename and prints
    its contents to stdout.
    """
    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end="")
