#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if not my_list:
        return
    elif not search:
        return my_list
    elif not replace:
        return my_list
    new_list = my_list
    for x, y in enumerate(my_list):
        if y == search:
            new_list[x] = replace
    return (new_list)
