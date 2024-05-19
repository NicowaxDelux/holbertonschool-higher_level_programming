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
        """int: length of square sides

        The setter validates that the size is an integer and is 0 or greater

        """
        return self.__size

    @size.setter
    def size(self, value):
        """size
         The size setter method update the size value of the square.

        Arg:
            value(int): value size

        Raise:
            TypeError: If `size` type is not `int`.

            ValueError: If `size` is less than `0`.

        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """tuple of int: the square's position on a plane

        The setter validates that the position is a tuple of 2 positive ints

        """

        return self.__position

    @position.setter
    def position(self, value):
        """position

        verify the positions with tuples

        Arg:
            value(int): value position

        Raise:
            TypeError: position must be a tuple of 2 positive integers

        """
        if (isinstance(value, tuple) and len(value) == 2 and
            isinstance(value[1], int) and isinstance(value[0], int) and
                value[0] >= 0 and value[1] >= 0):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        if not (isinstance(position, tuple) and
                len(position) == 2 and isinstance(position[0], int) and
                isinstance(position[1], int) and position[0] >= 0 and
                position[1] >= 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

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
            print("{}{}".format(" " * self.__position[0], "#" * self.__size))
