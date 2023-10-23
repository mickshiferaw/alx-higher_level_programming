#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for y in my_list:
            if my_list[y-1] <= x:
                return (y)
    except ValueError:
        print("fix some errors")
