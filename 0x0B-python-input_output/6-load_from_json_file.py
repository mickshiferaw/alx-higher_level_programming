#!/usr/bin/python3
""" a function that creates an Object from a “JSON file”"""
import json


def load_from_json_file(filename):
    """ a function that creates an Object from a “JSON file”
    Args:
        filename: a json file
    """
    with open(filename) as a_file:
        return json.load(a_file)
