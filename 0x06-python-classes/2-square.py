#!/usr/bin/python3
""" Class Square define a square"""


class Square:
    """Class Square """
    def __init__(self, size=0):
        self.__size = size
        if (type(self.__size) != int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
