#!/usr/bin/python3
for m in range(0, 100):
    print('{}'.format("%02d" % m), end="")
    if m < 99:
        print(end=", ")
