#!/usr/bin/python3
"""Square Class

square class

"""


class Square:
    """square class

    methods for manipulation

    """
    def __init__(self, size=0):
        """__init__

        initialize size value of square

        Args:
        size (int): size of the square

        raise:
        TypeError: size must be an integer
        ValueError: size must be >= 0

        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """return area of the square

        Return:
        the current square area

        """
        return self.__size **2
