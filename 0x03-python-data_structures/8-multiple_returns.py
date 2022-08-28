#!/usr/bin/python3

def multiple_returns(sentence):
    """
    Returns a tuple with the length of
    a string and its first character
    """
    character_count = 0
    if len(sentence) == 0:
        sentence[0] = None

    for letter in sentence:
        character_count += 1

    return (character_count, sentence[0])
