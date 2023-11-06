#!/usr/bin/python3
"""this is a class that raises an exception"""


class BaseGeometry:
    """this public instance method raise an exception"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """public instance method to validate value
        Args:
            name: is a string
            value: is an int
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """this is a sub class the inherits from BaseGeometry"""
    def __init__(self, width, height):
        """width and height are validated by integer_validator """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
