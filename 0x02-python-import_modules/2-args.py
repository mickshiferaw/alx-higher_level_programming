#!/usr/bin/python3
import sys

if len(sys.argv) == 1:
    print("argument", len(sys.argv))
elif len(sys.argv) == 0:
    print(len(sys.argv), "arguments.")

for m in sys.argv:
    print(m)
