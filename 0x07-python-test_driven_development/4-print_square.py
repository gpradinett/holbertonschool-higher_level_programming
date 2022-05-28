#!/usr/bin/python3
"""
Python function that prints a square with the character #
"""


def print_square(size):
    """
    Print square with the character #
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        for row in range(size):
            for columna in range(size):
                print("#", end="")
            print()
