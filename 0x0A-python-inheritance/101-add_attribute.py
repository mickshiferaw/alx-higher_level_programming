#!/usr/bin/python3
"""a function that adds a new attribute to an object if it’s possible"""


def attr(objct, attri, val):
    """adds a new attribute to an object if it’s possible
    Args:
        objct: an object
        attri: attribute to be added to object
        val: value of the attribute
    """
    if not hasattr(objct, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        setattr(objct, attri, val)
