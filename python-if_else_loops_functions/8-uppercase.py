#!/usr/bin/python3
def uppercase(str):
    new = ""
    for i in str:
        if ord('a') <= ord(i) <= ord('z'):
            i = ord(i) - 32
            new += chr(i)
        else:
            new += i
    print("{}".format(new))
