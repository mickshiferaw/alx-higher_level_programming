#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        return (None)
    else:
        fSentence = sentence[0]
        length = len(sentence)
        return ((f"({length}, {fSentence})"))
