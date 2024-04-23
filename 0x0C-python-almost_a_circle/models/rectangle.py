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
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        @property
        def width(self):
            """Getter method for width."""
            return self.__width

        @width.setter
        def width(self, value):
            """Setter method for width."""
            self.__width = value

        @property
        def height(self):
            """Getter method for height."""
            return self.__height

        @height.setter
        def height(self, value):
            """Setter method for height."""
            self.__height = value

        @property
        def x(self):
            """Getter method for x."""
            return self.__x

        @property
        def y(self):
            """Getter method for y."""
            return self.__y

        @x.setter
        def x(self, value):
            """Setter method for x."""
            self.__x = value

        @y.setter
        def y(self, value):
            """Setter method for y."""
            self.__y = value
