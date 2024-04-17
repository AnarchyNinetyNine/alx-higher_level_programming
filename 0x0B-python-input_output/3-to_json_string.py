#!/usr/bin/python3

"""
    Convert Python object to JSON string module.
"""


import json


def to_json_string(my_obj):

    """
    Converts a Python object to a JSON string representation.

    This function takes any Python object and converts it into
    a JSON string using the `json.dumps()` function
    from the `json` module.


    Args:
        my_obj: The Python object to be converted to a JSON string.


    Returns:
        str: A JSON string representing the input Python object.


    Example:
        Convert a dictionary object to a JSON string:

        >>> my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
        >>> json_string = to_json_string(my_dict)
        >>> print(json_string)
        '{"name": "John", "age": 30, "city": "New York"}'


    Note:
        - The `json.dumps()` function converts Python objects
          into JSON strings.
        - The returned JSON string represents the serialization
          of the input object.
        - This function can handle various Python data types
          like dictionaries, lists, strings, numbers, etc.

    """
    return json.dumps(my_obj)
