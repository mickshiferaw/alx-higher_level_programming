#!/usr/bin/python3
for m in reversed(range(97, 123)):
    if m % 2 == 0:
        print('{}'.format(chr(m  )), end="")
    else:
        print('{}'.format(chr(m - 32)), end="")
