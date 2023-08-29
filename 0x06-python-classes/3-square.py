#!/usr/bin/python3
""" This contains a square class"""


class Square:
    """Defining a square by size"""

    def __init__(self, size=0):
        """ Initialise a new square.

        Args:
        size (int): Size of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Prints area of the square"""
        return self.__size ** 2
