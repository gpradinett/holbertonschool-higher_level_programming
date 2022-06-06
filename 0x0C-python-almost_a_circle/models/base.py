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

        """
        if list_dictionaries is None or list_dictionaries == 0:
            return []

        return json.dumps(list_dictionaries)
