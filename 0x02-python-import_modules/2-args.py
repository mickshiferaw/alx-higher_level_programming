#!/usr/bin/python3
import sys
if len(sys.argv) - 1 == 1:
    for m in sys.argv:
        print(len(sys.argv), "argument:")
        print(m)
else:
    print(len(sys.argv) - 1, "arguments:")
    count = len(sys.argv) - 1
    for m in range(count): 
        print("{}: {}".format(m + 1, sys.argv[m + 1]))
