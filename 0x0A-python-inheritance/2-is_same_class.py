#!/usr/bin/python3
"""
Defines a function
"""


def is_same_class(obj, a_class):
    """
    A function that if an object is an instance of a class
    Args:
        obj: The object to be checked
        a_class: The class to check the object against
    Returns:
        True: if the object is an instance of the class
        False: otherwise
    """
    if not isinstance(a_class, type):
        raise TypeError("a_class must be a type")
    return (type(obj) is a_class)
