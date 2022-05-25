#!/usr/bin/python3
"""

"""


def text_indentation(text):
    """

    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    else:
        for i in ".:?":
            text = (i + "\n\n").join(
                    [line.strip(" ") for line in text.split(i)])
        print("{}".format(text), end="")
