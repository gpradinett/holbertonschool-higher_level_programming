#!/usr/bin/python3
"""
Define Rectangle class
"""


class Rectangle:
    """Rectangle """
    def __init__(self, width=0, height=0):
        """Initialization"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter func for private variable: width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set value for width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ Getter func for private variable: height """
        return self.__height

    @height.setter
    def height(self, value):
        """Set value for height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise TypeError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ Public instance method that returns the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """ Public instance method that returns the rectangle perimeter"""
        if self.__width == 0 or self.height == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)
