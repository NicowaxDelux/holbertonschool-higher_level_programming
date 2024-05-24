#!/usr/bin/python3
"""Rectangle  class

"""


class Rectangle:
    """Rectangle class

    methods,objets

    """
    def __init__(self, width=0, height=0):
        """method __init__

        Args:
            width(int): value width of rectangle
            height(int): value height of height
        """
        self.height = height
        self.width = width

    @property
    def height(self):
        """height getter

        Return:
            return value height of retangle (int)
        """
        return self.__height

    @height.setter
    def height(self, value):
        """height setter

        arg:
            value(int): value height

        Raises:
            TypeError: height must be an integer
            ValueError: height must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """width getter

            Reaturn:
            return value width of rectangle (int)
        """
        return self.__width

    @width.setter
    def width(self, value):
        """width setter

        arg:
            value(int): value width

        Raises:
            TypeError: width must be an integer
            ValueError: width must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """ area of rectangle

        Return:
            return area of rectangle width * height
        """
        return self.height * self.width

    def perimeter(self):
        """perimeter of rectangle

        Return:
            return perimeter of rectangle
        """
        if self.width == 0 or self.height == 0:
            return 0
        return ((self.width * 2) + (self.height * 2))
