#!/usr/bin/python3

"""
    Append command-line arguments to a JSON file module.
"""


import sys
import json


def add_item(filename):

    """
    Append command-line arguments to a JSON file.

    This function loads data from a JSON file, appends
    additional arguments from the command line, and then saves the updated data
    back to the same JSON file.

    Args:
        filename (str): The path to the JSON file from where the
                        serialized data will be retrieved and updated.


    Returns:
        None


    Raises:
        Exception: If there is an issue loading or saving the JSON file.

    """

    load = __import__('6-load_from_json_file').load_from_json_file
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

    try:
        data = load(filename)
    except Exception as e:
        data = []

    for arg in sys.argv[1:]:
        data.append(arg)

    save_to_json_file(data, filename)


add_item('add_item.json')
