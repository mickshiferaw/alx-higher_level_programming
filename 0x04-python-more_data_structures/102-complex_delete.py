#!/usr/bin/python3
def complex_delete(a_dictionary, value=''):
    listKy = list(a_dictionary.keys())
    for x in listKy:
        if value == a_dictionary.get(x):
            del a_dictionary[x]
    return (a_dictionary)
