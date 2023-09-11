#!/usr/bin/python3
"""
This function returns True if the object is exactly an instance of a class
"""


def is_same_class(obj, a_class):
    """
    Returns a boolean
    """
    if type(obj) is a_class:
        return True

    return False
