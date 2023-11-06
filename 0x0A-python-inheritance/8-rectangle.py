#!/usr/bin/python3
"""this is a class that raises an exception"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """this is a sub class the inherits from BaseGeometry"""
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        """width and height are validated by integer_validator """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
