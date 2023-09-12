#!/usr/bin/python3
"""
A class Student
"""


class Student:
    """Write a class Student that defines a student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
            Returns a dictionary
        """

        return (getattr(self, "__dict__"))
