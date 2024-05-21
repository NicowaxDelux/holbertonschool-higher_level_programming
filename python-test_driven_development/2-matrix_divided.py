#!/usr/bin/python3
"""This module defines the matrix_divided function.
The matrix_divided function divided matrix and div value integers
or floats, converting
them to integers.
"""


def matrix_divided(matrix, div):
    """ divided matrix with div values round 2 decimal places
        matrix / div
    """
    new_matrix = []

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

        new_row = []
        for element in row:
            if not isinstance(element, int) and not isinstance(element, float):
                raise TypeError("matrix must be a matrix\
 (list of lists) of integers/floats")

            result = round(element / div, 2)
            new_row.append(result)
        new_matrix.append(new_row)

    return new_matrix
