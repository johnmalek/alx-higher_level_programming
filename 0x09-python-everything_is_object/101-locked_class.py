#!/usr/bin/python3
"""
Class with no class or object attribute
that prevents user from dynamically creating
a new instance object
"""


class LockedClass:
    """
    A locked class that only lets the user dynamically
    create the instance attribute 'first_name
    """
    __slots__ = ["first_name"]

