#!/usr/bin/python3
"""a class Rectangle that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """this is a sub class the inherits from BaseGeometry"""
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        """width and height are validated by integer_validator """
        self.integer_validator("width", width)

        self.integer_validator("height", height)

    def area(self):
        """calculates the area of a rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """ str() should return, the following rectangle
            description: [Rectangle] <width>/<height>
        """
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
