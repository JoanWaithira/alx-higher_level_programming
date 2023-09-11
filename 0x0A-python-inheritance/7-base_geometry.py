#!/usr/bin/python3
"""
A class with an execption method
"""


class BaseGeometry:
    """A class raising an exception"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates a value

        Args:
        name: Always a string
        value:Always an integer and greater than 0

        Raises:
        TypeError: if value isn't an int
        ValueError if value is less than 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
