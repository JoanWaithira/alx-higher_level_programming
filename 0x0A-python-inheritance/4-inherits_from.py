#!/usr/bin/python3
"""
Write a function that returns True if the object is an instance of a class
that inherited (directly or indirectly) from the specified class
"""


def inherits_from(obj, a_class):
    """
    Returns boolean

    Args:
    obj: instance of a class
    a_class: class in question

    Return:
    True: If object is an instance of a class
    False: Otherwise
    """

    if type(obj) == a_class:
        return False

    return issubclass(type(obj), a_class)
