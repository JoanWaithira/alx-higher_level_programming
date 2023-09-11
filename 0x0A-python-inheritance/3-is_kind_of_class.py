#!/usr/bin/python3
"""
a function that returns True if the object is an instance
"""


def is_kind_of_class(obj, a_class):
    """
    REturns boolean based on condition
    """
    if type(obj) is a_class or issubclass(type(obj), a_class):
        return True

    return False
