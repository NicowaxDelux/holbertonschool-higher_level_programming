#!/usr/bin/python3
"""This funtion print 2 arguments strings
print two strings arguments 
"""


def say_my_name(first_name, last_name=""):
    """ funtion say_my_name have two arguments that
    print
    arg:
    first_name(str):first argument
    last_name(str):second argument

    Return:
    print first_name + last_name
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))
