#!/usr/bin/python3
"""
A function that returns aPython data structure
"""
import json


def from_json_string(my_str):
    """
    A function that returns a python data structure
    Args:
    str: The JSON string
    """
    return json.loads(my_str)
