#!/usr/bin/python3
"""
Defines a function
"""
import json


def save_to_json_file(my_obj, filename):
    """
    A function that writes an Object to a text file using JSON representation
    Args:
        my_obj: The object to be written to the file
        filename: The file to written to
    """
    with open(filename, mode="w", encoding="utf-8") as text_file:
        content = json.dumps(my_obj)
        return text_file.write(content)
