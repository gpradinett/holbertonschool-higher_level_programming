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

    @property
    def position(self):
        """
        Getter for position.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter for position.
        """

        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or type(value[1]) is not int or \
           value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """area: Returns the current square area"""
        return (self.__size*self.__size)
