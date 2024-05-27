#!/usr/bin/python3
"""class method
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
    """class Rectangle
    """
    def __init__(self, width, height):
        """__init__
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__heigth = height

    def area(self):
        """ method area

            Return: width * height
        """
        return self.__width * self.__heigth

    def __str__(self):
        """ __str__

            print [Rectangle] <width>/<height>
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__heigth)


class Square(Rectangle):
    def __init__(self, size):
        """__init_

            arg:
            size(int): size rectangle
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        """method __str__

        print [Square] <width>/<height>
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
