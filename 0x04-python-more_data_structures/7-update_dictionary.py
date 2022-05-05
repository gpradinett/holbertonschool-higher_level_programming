#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    new_key_value = {key: value}
    a_dictionary.update(new_key_value)
    return(a_dictionary)
