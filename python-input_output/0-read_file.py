#!/usr/bin/python3
"""method read file
"""

def read_file(filename=""):
    """ this funtion opens and reads contents of the file
    """
    with open(filename, encoding="utf-8") as file:
        read_file = file.read()
    print(read_file)
