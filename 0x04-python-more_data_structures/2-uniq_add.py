#!/usr/bin/python3

def uniq_add(my_list=[]):
    """ Adds all unique integers in a list"""
    uniq = list(set(my_list))
    sum = 0
    for i in uniq:
        sum += i
    return sum
