#!/usr/bin/python3
"""
A function that performs file writing
"""


def read_file(filename=""):
    """
    A function that writes a file

    Args:
    filename(str): filename of file to be read
    text: bytes to be written

    Returns:
    Number of characters written
    """

    with open(filename, "r", encoding="utf-8") as my_file:
        print(my_file.read(), end="")
