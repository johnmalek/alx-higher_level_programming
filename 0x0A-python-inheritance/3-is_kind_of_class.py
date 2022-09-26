#!/usr/bin/python3
"""
Defines a function
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of a class
    Args:
        obj: The object to be checked
        a_class: The class to check against
    Returns:
        True: If the object is an instance of the class
        False: Otherwise
    """
    if not isinstance(a_class, type):
        raise TypeError("a_class type must be type")
    if isinstance(obj, a_class) or issubclass(type(obj), a_class):
        return True
    return False
