#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    square = []
    for row in matrix:
        for elements in row:
            square.append(elements ** 2)
        new_matrix.append(square)
        square = []
    return new_matrix