#!/usr/bin/python3

def new_in_list(my_list, idx, element):

    """
    Replaces an element in a list at a specific 
    position without modifying the original list
    """

    if idx < 0:
        return my_list
    elif idx > len(my_list):
        return my_list
    else:
        original_list = my_list.copy()
        original_list[idx] = element
        return original_list
