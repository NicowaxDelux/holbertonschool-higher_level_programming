#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    result = {names: num * 2 for names, num in a_dictionary.items()}
    return result
