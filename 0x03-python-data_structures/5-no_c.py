#!/usr/bin/python3
def no_c(my_string):
    finalStr = ''
    for x in my_string:
        if x == 'c' or x== 'C':
            x=''
        finalStr += str(x)
    return (finalStr)
