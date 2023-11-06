#!/usr/bin/python3
"""a class MyInt that inherits from int"""


class MyInt(int):
    """a class MyInt that inherits from int"""
    def __eq__(self, val):
        """to invert == with !="""
        return self.real != val

    def __ne__(self, val):
        """to invert != to =="""
        return self.real == val
