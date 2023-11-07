#!/usr/bin/python3
"""a function that inserts a line of text to a file,"""


def append_after(filename="", search_string="", new_string=""):
    """a function that inserts a line of text to a file
    Args:
        filename: a file name
        search_string: a search string
        new_string: a new string
    """
    line_text = ""
    with open(filename) as a_file:
        for line in a_file:
            line_text += line
            if search_string in line:
                text += new_string
    with open(filename, mode="w") as a:
        a.write(text)
