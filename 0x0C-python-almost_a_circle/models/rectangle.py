#!/usr/bin/python3

"""
    Module defining the Rectangle class.

    This module contains the definition of the Rectangle class,
    which represents a geometric rectangle with specified width,
    height, position (x, y), and an optional identifier (ID). The
    Rectangle class inherits from the Base class and extends its
    functionality to manage rectangle-specific attributes.

    Classes:
        Rectangle: A class representing a rectangle with width, height,
        position, and identifier.

"""


from models.base import Base


class Rectangle(Base):

    """represents a rectangle object"""
    def __init__(self, width, height, x=0, y=0, id=None):

        """
        Initialize a Rectangle object.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the rectangle's
                               position (default is 0).
            y (int, optional): The y-coordinate of the rectangle's
                               position (default is 0).
            id (int, optional): The ID of the rectangle (default is None).
        """
        super().__init__(id)

        inpStr = ["width", "height", "x", "y"]
        inp = [width, height, x, y]
        sign = ""

        for inp_i, inpStr_i in zip(inp, inpStr):

            if not isinstance(inp_i, int):
                raise TypeError(f"{inpStr_i} must be an integer")

            if inp_i < 0:
                sign = ">=" if inpStr_i == "x" or inpStr_i == "y" else ">"
                raise ValueError(f"{inpStr_i} must be {sign} 0")

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter method for width."""
        return self.__width

    @property
    def height(self):
        """Getter method for height."""
        return self.__height

    @property
    def x(self):
        """Getter method for x."""
        return self.__x

    @property
    def y(self):
        """Getter method for y."""
        return self.__y

    @width.setter
    def width(self, value):
        """Setter method for width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Setter method for height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """Setter method for x."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """Setter method for y."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
