#!/usr/bin/python3
def remove_char_at(str, n):
    copy_str = ""
    str_len = len(str)
    for i in range(str_len):
        if i == n:
            continue
        copy_str += str[i]
    return copy_str
