#!/usr/bin/python3

"""Square module."""


class Square():

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

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Show the Square area


        Returns:
            int: The current Square Area.
        """
        return self.__size ** 2
