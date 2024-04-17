#!/usr/bin/python3

"""
    Convert JSON string to Python object module.
"""


import json


def from_json_string(my_str):

    """
    Converts a JSON string to a Python object.

    This function takes a JSON-formatted string
    and converts it into a corresponding Python object
    using the `json.loads()` function from the `json` module.


    Args:
        my_str (str): The JSON-formatted string
                      to be converted to a Python object.


    Returns:
        object: A Python object representing
                the deserialized JSON data.


    Example:
        Convert a JSON string to a dictionary object:

        >>> json_str = '{"name": "John", "age": 30, "city": "New York"}'
        >>> my_dict = from_json_string(json_str)
        >>> print(my_dict)
        {'name': 'John', 'age': 30, 'city': 'New York'}


    Note:
        - The `json.loads()` function converts a JSON-formatted string
          into a Python object.
        - This function can handle valid JSON strings representing
          dictionaries, lists, strings, numbers, booleans, and `null` values.
        - Invalid JSON strings will raise
          a `json.JSONDecodeError` during parsing.

    """
    return json.loads(my_str)
