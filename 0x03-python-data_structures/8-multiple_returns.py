#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence[0] is None:
        return
    length = len(sentence)
    return(length, sentence[0])
