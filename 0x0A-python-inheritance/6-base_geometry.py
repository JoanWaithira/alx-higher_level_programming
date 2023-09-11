#!/usr/bin/python3
"""
A class with an execption method
"""


class BaseGeometry:
    """A class raising an exception"""

    def area(self):
        raise Exception("area() is not implemented")
