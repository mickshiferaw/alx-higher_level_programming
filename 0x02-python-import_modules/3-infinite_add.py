#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    add = 0
    count = len(sys.argv) - 1
    for m in range(count):
        print(int(m + add))
