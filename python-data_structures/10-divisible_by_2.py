#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    copy_list = []
    for i in my_list:
        if i % 2 == 0:
            copy_list.append(True)
        else:
            copy_list.append(False)
    return copy_list
