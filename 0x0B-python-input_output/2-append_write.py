#!/usr/bin/python3
"""
a function that appends a string at the end of a text file (UTF8)
"""


def append_write(filename="", text=""):
    """
    A function that appends a string

    Args:
    filename(str): filename of file to be written to
    text: bytes of characters to be appended
    """
    with open(filename, mode="a", encoding="utf-8") as my_file:
        return (my_file.write(text))
