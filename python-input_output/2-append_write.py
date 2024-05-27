#!/usr/bin/python3
"""
    method append_write
"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file 

        If the file doesnt exist, it should be created
    """
    with open(filename,'a+', encoding="utf-8") as new_file:
        file = new_file.write(text)
    return file