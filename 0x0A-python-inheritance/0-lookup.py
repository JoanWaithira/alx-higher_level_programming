#!/usr/bin/python3
"""
A function that returns a list
"""


def lookup(obj):
    """Returns methods and attributes of an objects in a list
    Args:
    obj: a class or instance of class
    """
    return dir(obj)
