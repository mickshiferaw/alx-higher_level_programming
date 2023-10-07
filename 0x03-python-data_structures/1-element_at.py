#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0 or idx > (len(my_list)) - 1:
        return None
    else:
        print("Element at index {:d} is {}".format(idx, my_list[idx]))
print(element_at([1, 2, 3, 4, 5], 3))
