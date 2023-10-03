#!/usr/bin/python3
num = int(input("please inter a number: "))
def print_last_digit(num):
    num_st = repr(num)
    last_str = num_st[-1]
    last_digit = int(last_str)
    return (last_digit)
