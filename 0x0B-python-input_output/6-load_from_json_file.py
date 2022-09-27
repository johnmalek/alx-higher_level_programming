#!/usr/bin/python3
"""
Defines a class
"""
import json


def load_from_json_file(filename):
    """
    A function that creates an object from a JSON file
    Args:
        Filename: The file forom which to create an object
    """
    with open(filename, encoding="utf-8") as text_file:
        content = text_file.read()
        return json.loads(content)
