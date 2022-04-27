#!/usr/bin/python3
def remove_char_at(str, n):
    lon = len(str)
    if n > lon:
        return str
    if n >= 0:
        str = str.replace(str[n], "", 1)
        return str
    elif n < 0:
        return str
