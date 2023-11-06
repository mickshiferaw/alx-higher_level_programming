#!/usr/bin/python3
"""this is a class that raises an exception"""


class BaseGeometry:
    """this public instance method raise an exception"""
    def area(self):
        raise Exception("area() is not implemented")
