#!/usr/bin/python3

"""Write text to a file module."""


def write_file(filename="", text=""):

    """
    Write text to a file.

    This function writes the provided text to a file specified by the filename.


    Args:
        filename (str): The path to the file where the text will be written.
        text (str): The text to be written to the file.


    Returns:
        int: The number of characters written to the file.


    Raises:
        IOError: If there is an issue writing to the file.


    Example:
        To write the text "Hello, world!" to a file named 'output.txt':

        >>> write_file('output.txt', 'Hello, world!')
        13

    Note:
        - If the specified file does not exist, this function will create it.
        - If the file already exists, its previous content will be overwritten.
        - The function returns the number of characters written to the file.

    """
    with open(filename, 'w') as f:
        return f.write(text)
