#!/usr/bin/python3

"""
    Save Python object to JSON file module.
"""


import json


def save_to_json_file(my_obj, filename):

    """
    Serialize a Python object to JSON and save it to a file.

    Args:
        my_obj (object): The Python object to be serialized to JSON.
        filename (str): The path to the JSON file where
        the serialized data will be saved.


    Returns:
        None


    Raises:
        IOError: If there is an issue writing to the JSON file.


    Example:
        Serialize a dictionary object to a JSON file:

        >>> my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
        >>> save_to_json_file(my_dict, 'output.json')


    Note:
        - The `json.dumps()` function is used to serialize the Python object
          to a JSON-formatted string.
        - The serialized JSON string is then written to the specified file.
        - If the file already exists, its previous content will be overwritten.
        - The function does not return any value but saves
          the serialized JSON data to the specified file.

    """
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
