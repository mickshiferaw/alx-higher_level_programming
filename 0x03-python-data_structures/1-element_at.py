#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0 or int(idx) > len(my_list) - 1:
        return('none')
    else:
        return("Element at index {:d} is {}".format(idx, my_list[idx]))
