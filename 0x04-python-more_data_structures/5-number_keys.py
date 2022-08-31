#!/usr/bin/python3

def number_keys(a_dictionary):
    """Return the number of keys in a dictionary"""
    keys = 0
    for k, v in a_dictionary.items():
        keys += 1
    return (keys)
