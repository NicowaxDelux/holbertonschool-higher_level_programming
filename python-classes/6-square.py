#!/usr/bin/python3
"""Square Class

square class

"""


class Square:
    """square class

    methods for manipulation

    """
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (isinstance(value, tuple) and len(value) == 2 and
            isinstance(value[0], int) and isinstance(value[1], int) and
                value[0] >= 0 and value[1] >= 0):
            self.__position = value
        else:
            return TypeError("position must be a tuple of 2 positive integers")

    def __init__(self, size=0, position=(0, 0)):
        """__init__

        initialize size value of square

        Args:
        size (int): size square
        position (tuple): position square

        raise:
        TypeError: size must be an integer
        ValueError: size must be >= 0

        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        if (isinstance(position, tuple) and len(position) == 2 and
            isinstance(position[0], int) and isinstance(position[1], int) and
                position[0] >= 0 and position[1] >= 0):
            self.__position = position
        else:
            return TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """return area of the square

        Return:
        the current square area

        """
        return self.__size ** 2

    def my_print(self):
        """Public instance methodthat prints in stdout the
        square with the character #

        if size is equal to 0, print an empty line

        moves the sqaure to match position

        """
        if self.__size == 0:
            print()

        for _ in range(0, self.__position[1]):
            print()

        for _ in range(self.__size):
            print("{}{}".format("_" * self.__position[0], "#" * self.__size))
