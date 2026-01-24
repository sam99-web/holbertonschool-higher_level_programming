#!/usr/bin/pytho3

def multiple_returns(sentence):
    length = len(sentence)
    first = sentence[0] if sentence else None
    return (length, first)
