#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    newList = [val for val in my_list if isinstance(val, int)]
    count = 0
    for y in newList:
        try:
            if newList[y-1] <= x:
                print("{:d}".format(y), end="")
                count += 1
        except IndexError:
            return
    print()
    return (count)
