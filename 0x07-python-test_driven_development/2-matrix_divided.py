#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    A function that divides all elements of a matrix

    Args:
    matrix (list or lists): The matrix
    div (int or float): The divider

    Returns:
    A new matrix

    Raises:
    TypeError: if matrix is not a list/lists of integers or floats
    TypeError: If rows of matrices are not the same size
    TypeError: If the div is not an integer or a float
    ZeroDivisionError: If div is equal to zero
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("dividion by zero")

    new_matrix = [[round(element / div, 2) for element in row] for row in matrix]

    return new_matrix

