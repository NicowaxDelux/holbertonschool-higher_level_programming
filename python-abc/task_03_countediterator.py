#!/usr/bin/env python3
""" class CountedIterator
"""


class CountedIterator:
    """ class CountedIterator
    """

    def __init__(self, some_iterable):
        self.iterator = iter(some_iterable)
        self.counter = 0

    def __next__(self):
        try:
            item = next(self.iterator)
            self.counter += 1
            return item
        except StopIteration:
            raise StopIteration("no more items to iterate")

    def get_count(self):
        """ method get_count

            return the current value of the counter.
        """
        return self.counter
