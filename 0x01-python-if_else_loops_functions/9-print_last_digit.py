#!/usr/bin/python3
def print_last_digit(number):
    num_st = repr(number)
    last_str = num_st[-1]
    last_digit = int(last_str)
    return(last_digit)
