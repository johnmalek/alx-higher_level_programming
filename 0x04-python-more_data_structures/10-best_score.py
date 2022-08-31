#!/usr/bin/python3

def best_score(a_dictionary):
    """Returns a key with the biggest integer value"""
    if not a_dictionary:
        return
    biggest = 0
    for k, v in a_dictionary.items():
        if a_dictionary[k] > biggest:
            biggest = a_dictionary[k]
    for k, v in a_dictionary.items():
        if a_dictionary[k] == biggest:
            return (k)
