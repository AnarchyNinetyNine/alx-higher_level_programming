#!/usr/bin/python3

"""
    A module for safe integer printing with error handling.

    This module provides a function `safe_print_integer_err` that safely prints
    an integer value to stdout. If the input value is not an integer,
    it catches the exception and prints the error message to stderr.
"""


import sys


def safe_print_integer_err(value):
    """
    Safely prints an integer to stdout.

    Args:
        value (int): An integer value to be printed.

    Returns:
        bool: True if the value was successfully printed, False otherwise.

    Raises:
        ValueError: If `value` is not an integer.

    Usage:
        >>> from safe_printer import safe_print_integer_err

        >>> result = safe_print_integer_err(42)
        42

        >>> print(result)
        True

        >>> result = safe_print_integer_err('hello')
        Exception: invalid literal for int() with base 10: 'hello'

        >>> print(result)
        False
    """
    try:
        print("{:d}".format(value))
        return True
    except Exception as e:
        print(f"Exception: {e}", file=sys.stderr)
        return False
