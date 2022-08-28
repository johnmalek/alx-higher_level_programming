#!/usr/bin/python3

def multiple_returns(sentence):
    """
    Returns a tuple with the length of
    a string and its first character
    """
    if len(sentence) == 0:
        first = None
    else:
        first = sentence[0]
    return (len(sentence), first)
