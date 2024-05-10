#!/usr/bin/python3


def main():

    ascii_letter = 0
    for i in range(122, 96, -1):
        ascii_letter = i
        if i % 2 != 0:
            ascii_letter -= 32

        print(chr(ascii_letter), end="")


if __name__ == "__main__":
    main()
