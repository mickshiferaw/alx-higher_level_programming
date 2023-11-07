#!/usr/bin/python3
"""a function that reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """a function that reads a text file (UTF8) and prints it to stdout
    Args:
        filename: this is the name of the file
    """
    with open(filename, encoding="utf-8") as a_file:
        print(a_file.read())
