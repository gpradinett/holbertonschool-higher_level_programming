#!/usr/bin/python3
"""
creating a class Base
"""


import json
import os
import csv


class Base:
    """ class Base """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize id, increment class attribute __nb_objects if there is
        no id and set it as id.
        This class will be the “base” of all other classes in this project.
        The goal of it is to manage id attribute in all your future classes and
        to avoid duplicating the same code (by extension, same bugs)"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns a JSON representation of list_dictionaries.
        Args:
            - list_dictionaries: list of dicts
        Returns: JSON representation of the list

        
        if list_dictionaries is None or len(list_dictionaries) == 0:
            list_dictionaries = []

        return json.dumps(list_dictionaries)
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        
        if (type(list_dictionaries) != list or
           not all(type(x) == dict for x in list_dictionaries)):
            raise TypeError("list_dictionaries must be a list of dictionaries")
        return json.dumps(list_dictionaries)
    
    @classmethod
    def save_to_file(cls, list_objs):
        """

        """
        if list_objs is None or list_objs == []:
            jstr = "[]"
        else:
            jstr = cls.to_json_string([o.to_dictionary() for o in list_objs])
            filename = cls.__name__ + ".json"
        with open(filename, 'w') as f:
                f.write(jstr)
        
