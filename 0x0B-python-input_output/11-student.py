#!/usr/bin/python3
"""
Creates a Student class.
"""


class Student:
    """Class student"""
    def __init__(self, first_name, last_name, age):
        """Initialize student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Function that retrieves a dictionary representation of a Student"""
        if attrs is None:
            return self.__dict__
        else:
            dictionary = {}
            for attribute in attrs:
                if attribute in self.__dict__.keys():
                    dictionary[attribute] = self.__dict__[attribute]
            return dictionary

    def reload_from_json(self, json):
        """Function that replaces all attributes of a Student instance
        argument 'json' will always be a dictionary"""
        for key, value in json.items():
            setattr(self, key, value)
