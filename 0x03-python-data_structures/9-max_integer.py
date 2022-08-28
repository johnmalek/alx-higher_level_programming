#!/usr/bin/python3

def max_integer(my_list=[]):

    """
    Finds the biggest integer of a list
    """

    biggest = 0
    if len(my_list) == 0:
        return
    for item in my_list:
        if item > biggest:
            biggest = item
    return biggest
