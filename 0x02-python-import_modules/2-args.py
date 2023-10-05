#!/usr/bin/python3
import sys
count = len(sys.argv) - 1
if count == 1:
    print("1 argument:")
else:
    print('{} arguments:'.format(count))
for m in range(count):
        print("{}: {}".format(m + 1, sys.argv[m + 1]))
