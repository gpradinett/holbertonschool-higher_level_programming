#!/usr/bin/python3
"""
Define Rectangle class
"""


class Rectangle:
    """Rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialization"""
        self.width = width
        self.height = height
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
                string += str(self.print_symbol)
            string += "\n"
        return string[:-1]

    def __repr__(self):
        """
        """
        return f"Rectangle({self.width:d}, {self.height:d})"

    def __del__(self):
        """
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Static method that returns the biggest rectangle based on the area
        """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        elif rect_1.area() == rect_2.area():
            return rect_1
        elif rect_1.area() > rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """
        """
        return cls(width=size, height=size)
