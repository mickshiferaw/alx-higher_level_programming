#!/usr/bin/python3
""" a function that returns an object (Python data structure)"""
import json


def from_json_string(my_str):
    """ a function that returns an object (Python data structure)
    Args:
        my_str: a string
    """
    return json.loads(my_str)
