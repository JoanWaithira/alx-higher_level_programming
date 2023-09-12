#!/usr/bin/python3

"""
A function that writes an object
"""
import json


def save_to_json_file(my_obj, filename):
    """
    A function that writes an object
    Args:
    my_obj: My object
    filename: The name of file
    """
    with open(filename, "w+", encoding="utf-8") as my_file:
        json.dump(my_obj, my_file)
