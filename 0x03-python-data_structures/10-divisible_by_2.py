#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    
    """
    Finds all multiples of 2 in a list
    """
    if not my_list:
        return
    new_list = [item % 2 == 0 for item in my_list]
    return new_list
