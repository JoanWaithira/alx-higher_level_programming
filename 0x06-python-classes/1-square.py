#!/usr/bin/python3
""" This contains a square class"""


class Square:
    """Defining a square by size"""

    def __init__(self, size):
        """ Initialise a new square.

        Args:
        size (int): Size of square
        """

        self.__size = size
