#!/usr/bin/python3
"""
Define a rectangle class
"""


class Rectangle:
    """A class that represents a rectangle"""
    def __init__(self, width=0, height=0):
        """
        Initialise a new Rectangle

        Args:
        width (int): of the rectabgle
        height (int) of the rectangle
        """
        self.width = width
        self.height = height

        @property
        def width(self):
            """Get width of rectangle"""
            return self.__width

        @width.setter
        def width(self, value):
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            elif value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value

        @property
        def height(self):
            """GEt height of the rectangle"""
            return self.__height

        @height.setter
        def height(self, value):
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            elif value < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = value
