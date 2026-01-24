#!/usr/bin/pytho3

def multiple_returns(sentence):
    lengh = len(sentence)
    first = sentence[0] 
    if sentence == "":  
        return (0, None)
    return (len(sentence), sentence[0])

