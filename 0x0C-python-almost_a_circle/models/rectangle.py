#!/usr/bin/python3
"""
Create a Rectangle class, inheriting from Base.
"""
from models.base import Base


class Rectangle(Base):
    """ Class describing a rectangle.
    Public instance methods:
        - area()
        - display()
        - to_dictionary()
        - update()
    Inherits from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a Rectangle instance
        Args:
            - __width: width
            - __height: height
            - __x: position
            - __y: position
            - id: id

        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Retrieves the width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width attribute."""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height attribute"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Retrieves the x attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the x attribute"""

        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Retrieves the y attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the y attribute"""

        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Public instance method that returns the rectangle area
        Returns: area
        """
        return self.__width * self.__height

    def display(self):
        """Prints the Rectangle instance with the # character"""
        for y in range(0, self.__y):
            print()
        for row in range(0, self.__height):
            for x in range(0, self.__x):
                print(" ",  end="")
            for j in range(0, self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """Prints the Rectangle, we use the built in function
        __str__ - we will print with the format:
        [Rectangle] (<id>) <x>/<y> - <width>/<height>
        [Rectangle] lo vamos a hacer dinamico asi cuando otras clases hereden
        los atributos y metodos de esta clase puedan obtener el nombre de la
        clase correspondiente, como pasa cuando creamos mas adelante la class
        Square, al poner: self.__class__.__name__ logramos que cuando se quiera
        imprimir la class Square se imprima con el nombre de su clase: Square
        y no con Rectangle.
        """
        s = "[Rectangle]({}) {}/{} - {}/{}".format(
                self.id, self.__x, self.__y, self.__width, self.__height)
        return s

    def update(self, *args, **kwargs):
        """pdates attributes of an instance.
        Args:
            - id attribute
            - width attribute
            - height attribute
            - x attribute
            - y attribute
        This type of argument is called a “no-keyword argument” -
        Argument order is super important.
        """
        if args and args is not None:
            if len(args) >= 1:
                if type(args[0]) != int and args[0] is not None:
                    raise TypeError("id must be an integer")
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    if type(value) != int and value is not None:
                        raise TypeError("id must be an integer")
                    self.id = value
                if key == "width":
                    self.width = value
                if key == "height":
                    self.heigth = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
