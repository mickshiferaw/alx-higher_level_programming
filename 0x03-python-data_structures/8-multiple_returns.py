#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == '':
        return("First character: {}".format(None))
    else:
        fSentence = sentence[0]
        length = len(sentence)
        return("Length: {:d} - First character: {}".format(length, fSentence))
