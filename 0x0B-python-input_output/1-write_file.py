#!/usr/bin/python3
"""
A function that wroites a string to a text file`
"""


def write_file(filename="", text=""):
    """
    A function that writes a string

    Args:
        filename(str): filename of file to be read
        text: bytes to be written
    """
    with open(filename, "w", encoding="utf-8") as my_file:
        return my_file.write(text)
