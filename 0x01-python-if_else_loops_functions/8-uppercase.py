#!/usr/bin/python3
def uppercase(str):
    for m in str:
        print('{}'.format(chr(ord(m)-32)), end="")
    print()
