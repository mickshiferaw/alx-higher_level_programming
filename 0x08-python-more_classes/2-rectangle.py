#!/usr/bin/python3
"""this argument has two private instances; width and height"""


class Rectangle:
    """this class takes two private instance attribute
    Args:
    width: this is the width of the rectangle
    height: this is the height of the rectangle
    """
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        """this is the getter for height"""
    @property
    def height(self):
        return self.__height
    """this is the setter for height"""
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
    """this is the getter for width"""
    @property
    def width(self):
        return self.__width
    """this is the setter for width"""
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
    """this public instance method calculates the area"""
    def area(self):
        return self.width * self.height
    """this public instance method calculate the perimiter"""
    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width * self.height)
