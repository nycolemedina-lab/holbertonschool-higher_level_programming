#!/usr/bin/python3
"""
This module provides the matrix_divided function.
It divides all elements of a matrix by the variable div.
"""
def matrix_divided(matrix, div):
    """Divides all elements of a matrix by the variable div.

    Args:
        matrix: a list of lists of integers or floats
        div: an integer or float bigger than 0
    Returns:
        New matrix
    Raises:
        TypeError: if matrix is not a list of int or fl
        ZeroDivisionError: if div is 0
"""
    msg_type = "matrix must be a matrix (list of lists) of integers/floats"

    # Validate matrix is a list and non-empty
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(msg_type)

    row_len = None

    for row in matrix:
        # Validate each row is a list
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(msg_type)

        # Validate consistent row sizing
        if row_len is None:
            row_len = len(row)
        elif len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")

        # Validate elements inside the row (exclude booleans)
        for element in row:
            if not isinstance(element, (int, float)) or type(element) is bool:
                raise TypeError(msg_type)

    # Validate div type (exclude booleans)
    if not isinstance(div, (int, float)) or type(div) is bool:
        raise TypeError("div must be a number")

    # Validate div is not zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Return new matrix rounded to 2 decimal places using list comprehension
    return [[round(elem / div, 2) for elem in row] for row in matrix]
