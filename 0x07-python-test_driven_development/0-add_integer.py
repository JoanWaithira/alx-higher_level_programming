#!/usr/bin/python3

def add_integer(a, b=98):
    """
    A function that adds two integers

    Args:
    a (int or float): Teh first number.
    b (int or float): The second number

    Returns:
    int: The sum

    Raises:
    TypeError: if a or b is not an integer or a float
    """
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")

    return int(a + b)
