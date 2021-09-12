#!/usr/bin/python3


def multiple_returns(sentence):
    x = len(sentence)
    if x == 0:
        fir = "None"
    else:
        fir = sentence[0]
    
    z = x, fir
    return z
