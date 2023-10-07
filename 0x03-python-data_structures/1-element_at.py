#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0 or int(idx) > len(my_list) - 1:
        return('none')
    else:
        return("Element at index {} is {}".format(idx, my_list[idx]))
print(element_at([1, 2, 3, 4, 5], 3))
