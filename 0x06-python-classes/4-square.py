#!/usr/bin/python3

"""Square module."""


class Square:

    """
    Defines a square.


    Attributes:
        size (int): size of a square.
    """

    def __init__(self, size=0):

        """
        Initializes a new Square object.


        Args:
            size (int): size of a square.


        Raises:
            TypeError: If size is not of type integer.
            VAlueError: If size is less than 0
        """

        self.size = size

    @property
    def size(self):

        """Property to retrieve the Square's size."""

        return self.__size

    @size.setter
    def size(self, value):

        """
        Get the Square's size.


        Raises:
            TypeError: If size is not of type integer.
            VAlueError: If size is less than 0.
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):

        """
        Show the Square area


        Returns:
            int: The current Square Area.
        """

        return self.size ** 2
