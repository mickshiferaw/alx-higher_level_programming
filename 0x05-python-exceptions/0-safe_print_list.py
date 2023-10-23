#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    for y in range(x):
        try:
            print(my_list[y], end='')
        except IndexError:
            break
    print('')
    return
