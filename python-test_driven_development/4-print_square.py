#!/usr/bin/python3
""" this module  prints a square with the character #

print a square with size argument passed
"""


def print_square(size):
    """ this funtion print square with the character #

    arg:
    size(int): value size
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
