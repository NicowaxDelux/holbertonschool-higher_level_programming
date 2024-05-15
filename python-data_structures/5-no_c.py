#!/usr/bin/python3
def no_c(my_string):
    deletes_characters = ''
    for i in my_string:
        if i != 'c' and i != 'C':
            deletes_characters += i
    return deletes_characters
