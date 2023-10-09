#!/usr/bin/python3
""" This contains a square class"""


class Square:
    """Defining a square by size"""

    def __init__(self, size=0, position=(0, 0)):
        """ Initialise a new square.

        Args:
        size (int): Size of square
        position: Coordinates
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Private instant attribute size"""
        return(self.__size)

    @size.setter
    def size(self, value):
        """Setter method for size
        Args:
        value (int): Size of square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position (self, value):
        """ Setter method for position
        Args:
        Position: Coordinates
        """
        if not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(i,int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Prints area of the square"""
        return self.__size * self.__size

    def my_print(self):
        """print instant attribute size"""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
