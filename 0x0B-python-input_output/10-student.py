#!/usr/bin/python3
"""
Create a class Student that defines a student with: first_name, last_name
and age.
Has a public instance to_json that retrieves a dictionary representation of
a student.
"""


class Student:
    """Class that defines a student.
    Public attributes:
        - first_name
        - last_name
        - age
    Public method to_json().
    """
    def __init__(self, first_name, last_name, age):
        """Initialize student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

# Hasta aca es el mismo codigo que en el ejercicio anterior.
    def to_json(self, attrs=None):
        """Retrieves a dictionary representation
        of a Student instance."""
        if attrs is None:
            return self.__dict__
        else:
            dictionary = {}
            for attribute in attrs:
                # se refiere a las keys (del dict)
                if attribute in self.__dict__.keys():
                    # se refiere a las keys (del dict)
                    dictionary[attribute] = self.__dict__[attribute]
                    # se refiere a los valores (del dict)
            return dictionary
