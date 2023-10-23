#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    for y in my_list:
        try:
            if my_list[y-1] <= x:
                print(y, end='')
        except IndexError:
            print("fix some errors")
            break
    print()
