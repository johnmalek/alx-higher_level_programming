#!/usr/bin/python3
"""
Defines a function
"""
import json


def to_json_string(my_obj):
    """
    A function that returns a JSON representationof an onject
    Args:
        my_obj: The object to be returned as JSON
    Returns:
        The JSON representation of an object
    """
    return json.dumps(my_obj)
