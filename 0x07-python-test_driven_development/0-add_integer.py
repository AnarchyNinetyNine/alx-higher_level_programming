#!/usr/bin/python3

"""A module for 2 integers addition."""


def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a (int or float): The first number to be added. If float, it will be casted to int.
        b (int or float, optional): The second number to be added. Defaults to 98. If float, it will be casted to int.

    Returns:
        int: The sum of `a` and `b`, casted to an integer.

    Raises:
        TypeError: If `a` or `b` is not an integer or float.

    Examples:
        >>> add_integer(5, 3)
        8
        >>> add_integer(2.5, 4)
        6
        >>> add_integer(7, 8.2)
        15
        >>> add_integer(10.5, 3.5)
        14
        >>> add_integer('abc', 5)
        Traceback (most recent call last):
          ...
        TypeError: a must be an integer
        >>> add_integer(2, 'def')
        Traceback (most recent call last):
          ...
        TypeError: b must be an integer
    """

    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
