#!/usr/bin/python3
"""
    method is kind of class
"""


def is_kind_of_class(obj, a_class):
    """method 

    args:
        abj
        a_class

        Return:
        returns True if the object is an instance of, or if
        the object is an instance of a class that inherited from,
        the specified class ; otherwise False
    """
    return isinstance(obj, a_class)
