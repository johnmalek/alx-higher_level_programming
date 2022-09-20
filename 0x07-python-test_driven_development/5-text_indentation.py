#!/usr/bin/python3
"""
A function that prints two new lines
after .,? and :
"""


def text_indentation(text):
    """
    prints a string with 2 new lines after '.', '?', and ':'
    Args:
        text (int): text to print
    Raises:
        TypeError: "text must be a string"
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    string = text.replace('.', '.\n\n').replace(':', ':\n\n')\
        .replace('?', '?\n\n')
    for i in range(len(text)):
        string = string.replace('\n ', '\n')

    print(string, end='')
