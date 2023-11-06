#!/usr/bin/python3
"""a function that returns True if the object is an instance."""


def is_kind_of_class(obj, a_class):
    """a function that returns True if the object is an instance.
    Args:
        obj: an object
        a_class: a class
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
