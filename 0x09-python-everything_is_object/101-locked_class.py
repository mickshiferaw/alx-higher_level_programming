#!/usr/bin/python3
"""this is an empty class"""


class LockedClass:
    """prevents the user from dynamically creating new instance attributes"""
    __slots__ = ["first_name"]
