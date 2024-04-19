#!/usr/bin/python3

"""
    A module for safely executing functions with error handling.

    This module provides a function `safe_function` that safely
    executes a given function with specified arguments. If the
    function execution raises an exception, it catches the exception
    and prints the error message to stderr.
"""


import sys


def safe_function(fct, *args):
    """
    Safely executes a function with provided arguments.

    Args:
        fct (callable): The function to be executed.
        *args: Variable-length argument list to pass to `fct`.

    Returns:
        Any: The result of the function `fct` if successful, None otherwise.

    Raises:
        Exception: If an exception occurs during the execution of `fct`.

    Usage:
        >>> from safe_executor import safe_function

        >>> def my_div(a, b):
        ...     return a / b

        >>> result = safe_function(my_div, 10, 2)

        >>> print(result)
        5.0

        >>> result = safe_function(my_div, 10, 0)
        Exception: division by zero

        >>> print(result)
        None
    """
    try:
        return fct(*args)
    except Exception as e:
        print(f"Exception: {e.args[0]}", file=sys.stderr)
        return None
