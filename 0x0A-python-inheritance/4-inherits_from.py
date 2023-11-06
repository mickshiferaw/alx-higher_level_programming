#!/usr/bin/python3
"""a function that returns True if the object is an instance."""


def inherits_from(obj, a_class):
    """a function that returns True if the object is an instance.
    Args:
        obj: an object
        a_class: a class
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
