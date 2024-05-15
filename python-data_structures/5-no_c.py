#!/usr/bin/python3
def no_c(my_string):
    delete_character = my_string.translate({ord('c'): None}
                                           and {ord('C'): None})
    return delete_character
