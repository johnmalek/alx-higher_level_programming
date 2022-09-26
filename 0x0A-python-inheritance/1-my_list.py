#!/usr/bin/python3
"""
Defines a class
"""


class MyList(list):
    """
    A derived class that inherits from base class list
    """
    def print_sorted(self):
        """
        Prints the list in ascending order
        """
        self_copy = self[:]
        self_copy.sort()
        print(self_copy)
