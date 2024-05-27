#!/usr/bin/env python3
"""class VerboseList
"""


class VerboseList(list):
    """class verboselist
    """
    def append(self, item):
        print("Added [{}] to the list.".format(item))
        super().append(item)

    def extend(self, items):
        print("Extended the list with [{}] items.".format(len(items)))
        super().append(items)

    def remove(self, item):
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        if index == -1:
            popped_item = super().pop()
            if isinstance(popped_item, list):
                popped_item = popped_item[-1]
        else:
            popped_item = super().pop(index)
        print("Popped [{}] from the list.".format(popped_item))
        return popped_item
