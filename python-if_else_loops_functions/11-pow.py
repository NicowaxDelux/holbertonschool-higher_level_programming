#!/usr/bin/python3
def pow(a, b):

    if b == 0:
        return 1
    if b == 1:
        return a
    result = a
    for _ in range(1, abs(b)):
        if b > 0:
            result *= a
        if b < 0:
            result /= a * a * a
    return result
