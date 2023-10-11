#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if not key:
        return a_dictionary
    for key1 in a_dictionary.keys():
        if key1 == key:
            del a_dictionary[key]
            return (a_dictionary)
