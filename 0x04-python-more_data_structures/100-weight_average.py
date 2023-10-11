#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    weightt = 0
    multiply = 0
    for x in my_list:
        weightt += x[1]
        multiply += x[0] * x[1]
        final = multiply/weightt
    return (final)
