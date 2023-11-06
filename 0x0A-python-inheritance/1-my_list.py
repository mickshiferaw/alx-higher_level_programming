#!/usr/bin/python3
"""a class that inherits from list"""


class MyList(list):
    def print_sorted(self):
        """sorted method from a list will not change the original list"""
        print(sorted(self))
