#!/usr/bin/python3
"""a class that inherits from list"""


class MyList(list):
    """we can call the super class, but its unnessesary in this case"""
    def __init__(self):
        list.__init__(self)

    def print_sorted(self):
        """sorted method from a list will not change the original list"""
        print(sorted(self))
