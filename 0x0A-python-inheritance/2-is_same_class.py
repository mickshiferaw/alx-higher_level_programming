#!/usr/bin/python3
"""a func that checks if the object
    is exactly an instance of the specified class"""


def is_same_class(obj, a_class):
    """a func that checks if the object
    is exactly an instance of the specified class
    Args:
        obj: an object
        a_class: a class
    """
    if type(obj) == a_class:
        return True
    else:
        return False
