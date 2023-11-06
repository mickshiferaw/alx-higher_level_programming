#!/usr/bin/python3
"""Defines  a class Square that inherits from Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """init the new square class"""
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)

        super().__init__(size, size)
