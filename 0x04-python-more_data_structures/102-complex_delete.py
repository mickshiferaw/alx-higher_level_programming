#!/usr/bin/python3
def complex_delete(a_dictionary, value=''):
    newdict = a_dictionary.copy()
    if not value:
        return a_dictionary
    for x, y in a_dictionary.items():
        if value == x:
            del newdict[x]
    for k, m in newdict.items():
        print(k, m)
