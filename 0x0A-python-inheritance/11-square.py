#!/usr/bin/python3
"""Defines  a class Square that inherits from Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)

        super().__init__(size, size)

    def __str__(self):
        """ str() should return, the following rectangle
            description: [Square] <size>/<size>
        """
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__size) + "/" + str(self.__size)
        return string
