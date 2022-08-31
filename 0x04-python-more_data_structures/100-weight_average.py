#!/usr/bin/python3

def weight_average(my_list=[]):
    if len(my_list) == 0:
        return (0)

    first_div = 0
    second_div = 0
    for tple in my_list:
        first_div += (tple[0] * tple[1])
        second_div += tple[1]
    weighted_average = first_div / second_div
    return (weighted_average)
