#!/usr/bin/python3
""" Class Square define a square """


class Square:
    """ Class define a square """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """ get """
        return self.__size

    @size.setter
    def size(self, value):
        """ update"""
        if (type(value)) is not int:
            raise TypeError('size must be an integer')
        elif (value < 0):
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        return (self.__size*self.__size)

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for row in range(self.__size):
                for column in range(self.__size):
                    print("#", end="")
                print()
