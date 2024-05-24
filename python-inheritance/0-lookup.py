#!/usr/bin/python3
"""method lookup

function that returns the list of available
attributes and methods of an object:
"""


def lookup(obj):
    """lookup of list
    arg:
        object
    """
    return dir(obj)
