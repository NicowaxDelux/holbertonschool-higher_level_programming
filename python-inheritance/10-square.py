#!/usr/bin/python3
"""Square Module
"""


class BaseGeometry:
    """class BaseGeometry
    """
    def area(self):
        """ method area

        Raise: Exception with the message area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Public instance  that validates value

            Args:
                name (string): name
                value(int): Value
            Raises:
                TypeError: When Value is not int
                ValueError: When Value less or equal to 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Class Rectangle
    """
    def __init__(self, width, height):
        """__init__
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__heigth = height

    def area(self):
        """method area

            Return: width * height
        """
        return self.__width * self.__heigth

    def __str__(self):
        """ __str__

            print [Rectangle] <width>/<height>
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__heigth)


class Square(Rectangle):
    """
        Square Class
    """
    def __init__(self, size):
        """
            Initialize the square base on Rectangle
        """
        self.__size = size
        self.integer_validator('size', self.__size)

    def area(self):
        """
        define area of the square
        """
        return self.__size ** 2

    def __str__(self):
        """
            __str__
        """
        return ("[Rectangle] {}/{}".format(self.__size, self.__size))
