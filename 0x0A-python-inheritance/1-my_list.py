#!/usr/bin/python3
"""
It contains a class inheriting from list class
"""


class MyList(list):
    """
    class inherits from a list class and does the ascending sort
    """

    def print_sorted(self):
        """the sorted list"""
        print(sorted(self))
