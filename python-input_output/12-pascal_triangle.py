#!/usr/bin/python3
"""
    method pascal triangle
"""


def pascal_triangle(n):
    """
        returns a list of lists of integers representing
        the Pascal-s triangle of n
    """
    if n <= 0:
        return []

    new_list = []
    temp = []
    for x in range(n):
        row = []
        for y in range(x + 1):
            if x == 0 or y == 0 or x == y:
                row.append(1)
            else:
                row.append(temp[y] + temp[y - 1])
        temp = row
        new_list.append(row)
    return new_list
