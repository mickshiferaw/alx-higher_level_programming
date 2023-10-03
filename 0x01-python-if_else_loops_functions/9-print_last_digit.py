#!/usr/bin/python3
def print_last_digit(number):
    num_st = repr(number)
    last_str = num_st[-1]
    last_digit = int(last_str)
    if number < 0:
        return (-last_digit)
    return (last_digit)
