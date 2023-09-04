#!/usr/bin/python3
"""
Define a rectangle class
"""


class Rectangle:
    """A class that represents a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialise a new Rectangle

        Args:
        width (int): of the rectabgle
        height (int) of the rectangle
        """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Get width of rectangle

        Returns:
        int: The width

        Raises:
        TypeError: if value is not an integer
        ValueError: if value is less than zero
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Get height of the rectangle


        Returns:
        int:the height

        Raises:
        TypeError: if value is not an integer
        ValueError: if value is less than zero

        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def my_print(self):
        if self.__width == 0 or self.__height == 0:
            return ("")
        rectangle_str = ""
        for row in range(self.__height):
            rectangle_str += str(self.print_symbol) * self.__width + "\n"
        return rectangle_str.rstrip()

    def __str__(self):
        """
        Return string representation
        """
        return ("{}".format(self.my_print()))

    def __repr__(self):
        return ("Rectangle({}, {})".format(str(self.width), str(self.height)))

    def __del__(self):
        """
        Destructor of the instance of class Rectangle
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Returns the instance of rectangele with larger area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return (rect_1)
        else:
            return (rect_2)

    @classmethod
    def square(cls, size=0):
        """ REturn a new class with width and height
        width == height == size"""
        return cls(size, size)
