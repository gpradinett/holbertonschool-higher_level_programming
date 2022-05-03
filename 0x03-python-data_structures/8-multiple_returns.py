#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        return (0, None)
    else:
        length = len(sentence)
        first_letter = sentence[0]
        new_tuple = (length, first_letter)
        return new_tuple
