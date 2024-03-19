#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence or len(sentence) == 0:
        return (None, None)
    return(len(sentence), sentence[0])
