#!/usr/bin/python3

"""This module contains a Base class."""


class Base:

    """
    A base class for managing object IDs.

    Attributes:
        __nb_objects (int): A private class variable to track
                            the number of objects created.
        id (int): The unique identifier assigned to each instance of the class.
    """

    __nb_objects = 0

    def __init__(self, id=None):

        """
        Initialize a Base object.

        Args:
            id (int, optional): The desired ID for the object.
                                If not provided, a new ID will be assigned.

        Note:
            If `id` is not specified, the object will automatically be assigned
            a unique ID based on the number of objects created so far.
        """
        if id:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects
