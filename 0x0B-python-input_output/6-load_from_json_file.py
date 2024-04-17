#!/usr/bin/python3

"""
    Load Python object from JSON file module.
"""

import json


def load_from_json_file(filename):

    """
    Deserialize a JSON file to a Python object.

    Args:
        filename (str): The path to the JSON file to be loaded.


    Returns:
        object: The Python object representing the deserialized JSON data.


    Raises:
        FileNotFoundError: If the specified file does not exist.
        IOError: If there is an issue reading from the JSON file.
        json.JSONDecodeError: If the JSON data in the file is invalid.


    Example:
        Deserialize a JSON file into a dictionary object:

        >>> loaded_dict = load_from_json_file('data.json')
        >>> print(loaded_dict)
        {'name': 'John', 'age': 30, 'city': 'New York'}


    Note:
        - The `json.load()` function is used to deserialize the JSON data from
          the file into a Python object.
        - This function assumes that the JSON data in the file represents
          a valid JSON structure.
        - It raises appropriate exceptions if the file is not found,
          cannot be read, or contains invalid JSON.

    """
    with open(filename, 'r') as f:
        return json.load(f)
