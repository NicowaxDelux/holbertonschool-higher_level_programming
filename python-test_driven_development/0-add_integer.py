#!/usr/bin/python3
"""This module defines the add_integer function.

The add_integer function adds two integers or floats, converting
them to integers if necessary.
"""


def add_integer(a, b=98):
    """add integer
    a(int):number + b(int):number
    """
    if not isinstance(a, float) and not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, float) and not isinstance(b, int):
        raise TypeError("b must be an integer")

    if a > 1000000 or (a == float('inf') or a == float('-inf')):
        raise OverflowError("cannot convert float infinity to integer")
    a = int(a)

    if b > 1000000 or (b == float('inf') or b == float('-inf')):
        raise OverflowError("cannot convert float infinity to integer")
    b = int(b)

    return a + b
