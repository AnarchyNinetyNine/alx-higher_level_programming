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
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be > 0")
        self.width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be > 0")

        self.height = height

        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be > 0")
        self.x = x

        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be > 0")
        self.y = y

        super().__init__(id)

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
