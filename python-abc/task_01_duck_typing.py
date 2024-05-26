#!/usr/bin/env python3
"""Shapes, Interfaces, and Duck Typing
"""
from abc import ABC, abstractmethod


class Shape(ABC):
    """Shape class
    """
    @abstractmethod
    def area(self):
        pass

    def perimeter(self):
        pass


class Circle(Shape):
    """circle
    """
    def __init__(self, radius):

        self.__radius = radius

    def area(self):
        """circle area

            return circle area
        """
        return 3.141592653589793 * self.__radius ** 2

    def perimeter(self):
        """perimeter

            return circle perimeter
        """
        if self.perimeter < 0:
            return 0
        return 2 * 3.141592653589793 * self.__radius


class Rectangle(Shape):
    """ Rectangle class
    """
    def __init__(self, width, height):

        self.__width = width
        self.__height = height

    def area(self):
        """ method area

            return width * heigh
        """
        return self.__width * self.__height

    def perimeter(self):
        """ method perimeter

            return 2(width + height)
        """
        return 2 * (self.__width + self.__height)


def shape_info(shape):
    """Print the area and perimeter of the
    shape passed to the function.
    """
    try:
        area = shape.area()
        perimeter = shape.perimeter()

        print("Area: {}".format(area))
        print("Perimeter: {}".format(perimeter))

    except AttributeError as e:
        print(f"Error: {e}")
