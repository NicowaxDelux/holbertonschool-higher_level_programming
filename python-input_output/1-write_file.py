#!/usr/bin/python3
""" method write file 
    file: my_first_file.txt
"""


def write_file(filename="", text=""):
    """ write file

    args:
        filename: my_first_file.txt
        text: text to write
    """
    with open(filename, 'w', encoding="utf-8") as file:
        write = file.write(text)
    return write