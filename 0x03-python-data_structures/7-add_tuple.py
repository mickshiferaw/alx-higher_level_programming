#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    newA = list(tuple_a)
    newB = list(tuple_b)
    if len(newA) == 0 and len(newB) == 0:
        newA.append(0)
        newB.append(0)
        add1 = newA[0] + newB[0]
        add2 = newA[0] + newB[0]
        return ((add1, add2))
    if len(newA) < 1:
        newA.append(0)
        add1 = newA[0] + newB[0]
        add2 = newA[0] + newB[1]
        return ((add1, add2))
    if len(newB) < 1:
        newB.append(0)
        add1 = newA[0] + newB[0]
        add2 = newA[1] + newB[0]
        return ((add1, add2))
    elif len(newA) < 2 or len(newB) < 2:
        newA.append(0)
        newB.append(0)
        add1 = newA[0] + newB[0]
        add2 = newA[1] + newB[1]
        return ((add1, add2))
    elif len(newA) > 2 or len(newB) > 2:
        add1 = newA[0] + newB[0]
        add2 = newA[1] + newB[1]
        return ((add1, add2))
    else:
        add1 = newA[0] + newB[0]
        add2 = newA[1] + newB[1]
        return ((add1, add2))
