#!/usr/bin/python3
"""
Defines a function
"""


def lookup(obj):
    """
    A function that returns the list of available attributes
    and methods of an object
    Args:
        obj: The object to return attributes and methods
    Returns:
        Attributes and methods of the object as a list
    """
    return dir(obj)
