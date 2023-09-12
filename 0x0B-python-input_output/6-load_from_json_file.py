#!/usr/bin/python3
"""
A function that creates an object from a json file
"""
import json


def load_from_json_file(filename):
    """
    Write a function that creates an Object from a “JSON file”:

    Args:
    filename(str): json file
    """
    with open(filename, "r+", encoding="utf-8") as my_file:
        return (json.load(my_file))
