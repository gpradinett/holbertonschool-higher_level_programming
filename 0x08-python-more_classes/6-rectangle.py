#!/usr/bin/python3
"""
Define Rectangle class
"""


class Rectangle:
    """Rectangle"""
    number_of_instances = 0
    # Se incializa aca y no en el init porque es un atributo de toda la clase

    def __init__(self, width=0, height=0):
        """Initialization"""
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1
        """
        """

    @property
    def height(self):
        """
        Getter func for private variable: height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set value for: height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        """
        Getter func for private variable: width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set value for: width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    def area(self):
        """
        Public instance method that returns the rectangle area
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Public instance method that returns the rectangle perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """
        """
        string = ""
        if self.width == 0 or self.height == 0:
            return string
        for height in range(self.__height):
            for width in range(self.__width):
                string += "#"
            string += "\n"
        return string[:-1]

    def __repr__(self):
        """
        """
        return f"Rectangle({self.width:d}, {self.height:d})"

    def __del__(self):
        """
        Use of del method to delete an isntance of a class and print a message
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
