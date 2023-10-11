#!/usr/bin/python3
def search_replace(my_list=[], search=None, replace=None):
    new_list = my_list
    for x, y in enumerate(my_list):
        if y == search:
            new_list[x] = replace
    return (new_list)
