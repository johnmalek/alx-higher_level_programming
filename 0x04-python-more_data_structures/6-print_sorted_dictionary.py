#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """Prints a dictionary by ordered keys"""
    for k in sorted(a_dictionary.keys()):
        print("{}: {}".format(k, a_dictionary[k]))
