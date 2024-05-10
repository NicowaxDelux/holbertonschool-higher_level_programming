#!/usr/bin/python3
def fizzbuzz():
    for number in range(1, 101):
        if number % 3 != 0 and number % 5 != 0:
            print(f"{number} ", end="")
            continue

        if number % 3 == 0:
            print("Fizz",  end="")

        if number % 5 == 0:
            print("Buzz", end="")

        print(" ", end="")

    return number
