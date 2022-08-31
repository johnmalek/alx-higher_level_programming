#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    """Returns a set of all elements present in only one set"""
    only_diff = set_1 ^ set_2
    return (only_diff)
