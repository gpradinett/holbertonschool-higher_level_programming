#!/usr/bin/python3
"""
Python function that prints a text with 2 new lines
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    else:
        for i in ".:?":
            text = (i + "\n\n").join(
                    [line.strip(" ") for line in text.split(i)])
        print("{}".format(text), end="")
