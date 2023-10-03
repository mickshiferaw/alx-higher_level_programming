#!/usr/bin/python3
def islower(c):
    data = (ord(c))
    if data > 96 and data < 124:
        print(f"{c} is lower")
        return (True)
    else:
        print(f"{c} is upper")
        return (False)
