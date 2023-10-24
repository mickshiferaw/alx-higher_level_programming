#!/usr/bin/python3
""" define a class named square.
    @size is a private attribute.
    @area is a method that calculates the area.
"""


class Square:
    """
    this is a first class task.
    this class doesnt do anything.
    @size is a private attribute.
    @area is a method that calculates the area.
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.size = size

    def area(self):
        if not isinstance(self.size, int):
            raise TypeError('size must be an integer')
        return self.size * self.size
