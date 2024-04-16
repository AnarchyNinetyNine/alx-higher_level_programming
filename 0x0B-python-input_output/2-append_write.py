#!/usr/bin/python3

"""
    Append text to a file module.
"""


def append_write(filename="", text=""):

    """
    Append text to the end of a file.

    This function appends the provided text to the end of a file
    specified by the filename.


    Args:
        filename (str): The path to the file where the text will be appended.
        text (str): The text to be appended to the file.


    Returns:
        int: The number of characters appended to the file.


    Raises:
        IOError: If there is an issue appending to the file.


    Example:
        To append the text "Additional text" to a file named 'data.txt':

        >>> append_write('data.txt', 'Additional text')
        15


    Note:
        - If the specified file does not exist, this function will create it.
        - The function opens the file in append mode ('a'), which means
          new content will be added to the end of the file without overwriting
          existing content.
        - The function returns the number of characters appended to the file.

    """
    with open(filename, 'a') as f:
        return f.write(text)
