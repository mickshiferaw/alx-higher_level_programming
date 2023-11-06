#!/usr/bin/python3
"""a function that adds a new attribute to an object if it’s possible"""


def add_attribute(objct, attri, val):
    """adds a new attribute to an object if it’s possible

    Args:
        objct: an object
        attri: attribute to be added to object
        val: value of the attribute
    Exception:
        TypeError: if the attr can not be added
    """
    if not hasattr(objct, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        setattr(objct, attri, val)
