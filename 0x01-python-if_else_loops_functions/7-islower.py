#!/usr/bin/python3
def islower(fid):
    data = (ord(fid))
    print(data)
    if data > 97 and data < 124:
        return (True)
    else:
        return (False)
