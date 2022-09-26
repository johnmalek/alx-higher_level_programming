#!/usr/bin/python3
"""
Defines a function
"""


def inherits_from(obj, a_class):
    """
    Checks if an object is an instance of a class that it
    inherited from
    Args:
        obj: The object to be checked
        a_class: The class to check against
    Returns:
        True: If the object is an instance of the class
        False: otherwise
    """
    if not isinstance(a_class, type):
        raise TypeError("a_class must be a type")
    return (issubclass(type(obj), a_class) and type(obj) is not a_class)
