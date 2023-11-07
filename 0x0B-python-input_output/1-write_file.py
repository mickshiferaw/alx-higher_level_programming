#!/usr/bin/python3
"""a function that writes a string to a text file"""


def write_file(filename="", text=""):
    """a function that writes a string to a text file
    Args:
        filename: this is the name of the file
        text: a text that will be written into the file
    """
    with open(filename, mode="w", encoding="utf-8") as a_file:
        return a_file.write(text)
