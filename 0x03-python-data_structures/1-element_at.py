#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0 or int(idx) > len(my_list) - 1:
        print('none')
    else:
        print("Element at index {:d} is {}".format(idx, my_list[idx]))
