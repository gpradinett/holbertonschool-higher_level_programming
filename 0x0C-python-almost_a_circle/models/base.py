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
        Writes the JSON string representation of
        list_objs to a file.
        Args:
            - list_objs: list of instances who inherits of Base
        """
        filename = cls.__name__ + ".json"
        string = []
        with open(filename, "w") as f:
            if list_objs is None or list_objs == []:
                f.write(cls.to_json_string(string))

            else:
                for i in list_objs:
                    string.append(cls.to_dictionary(i))

                f.write(cls.to_json_string(string))

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation json_string.
        Args:
            - json_string: string to convert to list
        """
        if json_string is None or len(json_string) == 0:
            return []

        else:
            list_json = json.loads(json_string)
            return list_json

    @classmethod
    def create(cls, **dictionary):
        """
        This is a class method that returns an instance (object) with all
        attributes already set.
        Inside "**dictionary" are the keys and values to set to the new
        instance.
        We are going to use the method "update" that was created in the other
        classes (Rectangle and Square).
        """
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        class method def load_from_file(cls):
        which returns a
        list of instances
        """
        list_ = []
        filename = cls.__name__ + ".json"
        if os.path.exists(filename):
            with open(filename, "r") as f:
                dictionary = cls.from_json_string(f.read())

            for i in dictionary:
                list_.append(cls.create(**i))

            return list_

        else:
            return list_
