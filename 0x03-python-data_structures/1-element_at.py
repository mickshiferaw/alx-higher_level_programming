#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0 or idx > (len(my_list)) - 1:
        return None
    return("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))
