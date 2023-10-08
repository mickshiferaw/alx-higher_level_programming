#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    newA = list(tuple_a)
    newB = list(tuple_b)
    if len(newA) < 2 or len(newB) < 2:
        newA.append(0)
        newB.append(0)
    if len(newA) > 2 or len(newB) > 2:
        tuppleAdd1 = newA[0] + newB[0]
        tuppleAdd2 = newA[1] + newB[1]
    return ((tuppleAdd1, tuppleAdd2))
