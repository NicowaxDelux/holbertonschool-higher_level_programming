#!/usr/bin/python3
"""Rectangle  class

"""


class Rectangle:
    """Rectangle class

    methods,objets

    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """method __init__

        Args:
            width(int): value width of rectangle
            height(int): value height of height
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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
        return self.__height * self.__width

    def perimeter(self):
        """perimeter of rectangle

        Return:
            return perimeter of rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """print print the rectangle with the character #

        if width or height is equal to 0, return an empty string
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        symbol = str(self.print_symbol)
        return ((symbol * self.__width + "\n") * self.__height)[:-1]

    def __repr__(self):
        """string representation of the rectangle

        Return:
            representation of the rectangle
        """
        return 'Rectangle({}, {})'.format(self.width, self.height)

    def __del__(self):
        """Delete instance rectangle
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """bigger_or_equal

        args:
            rect1: my_rectangle_1
            rect2: my_rectangle_2
        returns:
            returns the biggest rectangle based on the area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """ new square
        arg:
            size: size of the square

        Return:
             returns a new Rectangle instance with width == height == size
        """
        return cls(size, size)
