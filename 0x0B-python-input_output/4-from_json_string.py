#!/usr/bin/python3
"""
Defines a function
"""
import json


def from_json_string(my_str):
    """
    A function that returns an object represented by a JSON string
    Args:
        my_str: The string to convert to object
    Returns:
        An object represented by JSON string
    """
    return json.loads(my_str)
