#!/usr/bin/python3
""" a function that returns an object (Python data structure)"""
import json


def save_to_json_file(my_obj, filename):
    """ a function that returns an object (Python data structure)
    Args:
        my_str: a string
    """
    with open(filename, mode="w", encoding="utf-8") as a_file:
        return a_file.write(json.dumps(my_obj))
