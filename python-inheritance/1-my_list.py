#!/usr/bin/python3
"""
    method that inherits from list
"""


class MyList(list):

    def print_sorted(self):
        """
            that prints the list, but sorted
        """
        print(sorted(self))
