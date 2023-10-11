#!/usr/bin/python3
def search_replace(my_list=[], search=None, replace=None):
    if not my_list:
        return
    if replace is None:
        return my_list
    new_list = my_list.copy()
    for x, y in enumerate(new_list):
        if y == search:
            new_list[x] = replace
    return (new_list)
