#!/usr/bin/python3
"""
 a function that returns the dictionary description
"""


def class_to_json(obj):
    """
    A function tha returns the dictionary description
    Args:
    obj: An instance of a class
    """
    return (getattr(obj, "__dict__"))
