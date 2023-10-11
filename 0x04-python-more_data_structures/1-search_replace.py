#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if not my_list:
        return
    for x, y in enumerate(my_list):
        if y == search:
            my_list[x] = replace
    return (my_list)
