#!/usr/bin/python3
def multiple_returns(sentence=''):
    if len(sentence) == 0:
        first = None
        return (first)
    else:
        first = sentence[0]
        length = len(sentence)
        return ((length, first))
