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

    if isinstance(a, float):
        if a == float('inf') or a == float('-inf'):
            raise OverflowError("cannot convert float infinity to interger")
        a = int(a)

    if isinstance(b, float):
        if b == float('inf') or b == float('-inf'):
            raise OverflowError("cannot convert float infinity to interger")
        b = int(b)

    return a + b
