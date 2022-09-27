#!/usr/bin/python3
"""
Defines a class
"""


def append_write(filename="", text=""):
    """
    A function that appends a string at the end of a text file
    Args:
        filename: File to appended to
        text: text to append
    Returns:
        The number of characters added
    """
    with open(filename, mode="a", encoding="utf-8") as text_file:
        content = text_file.write(text)
        return len(text)
