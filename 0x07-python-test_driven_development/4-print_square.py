#!/usr/bin/python3
"""this function prints a square with a the charactor #"""


def print_square(size):
    """this function prints a square with the charactor #"""
    # if not size:
    #     raise TypeError("missing argument")
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    if not isinstance(size, int) and size < 0:
        raise TypeError('size must be an integer')
    for x in range(size):
        print("#" * size)
