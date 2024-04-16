#!/usr/bin/python3

"""
    A module for reading and printing the contents of a text file.

    This module provides a function to read the contents of a
    text file and print each line.
"""


def read_file(filename=""):

    """
    Read and print the contents of a text file line by line.

    Args:
        filename (str): The path to the text file to be read. If not provided,
            an empty string, or a path that evaluates to False will result in
            an attempt to read from standard input.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        IOError: If there is an issue reading the file.

    Example:
        To read and print the contents of a file named 'example.txt':

        >>> read_file('my_file_0001.txt')
        We offer a truly innovative approach to education:
        focus on building reliable applications and scalable systems,
        take on real-world challenges, collaborate with your peers.
        ...
        A school every software engineer would have dreamt of!

    Note:
        This function assumes the file is encoded in UTF-8 and reads it
        in text mode. It prints each line after stripping any trailing
        whitespace characters (like '\n').

    """
    with open(filename, 'rt') as text_file:
        print(text_file.read(), end="")
