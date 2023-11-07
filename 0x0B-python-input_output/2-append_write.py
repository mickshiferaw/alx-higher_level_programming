#!/usr/bin/python3
"""a function that appends a string to a text file"""


def append_write(filename="", text=""):
    """a function that appends a string to a text file
    Args:
        filename: this is the name of the file
        text: a text that will be appended into the file
    """
    with open(filename, mode="a", encoding="utf-8") as a_file:
        return a_file.write(text)
