#!/usr/bin/python3
"""a class representing a student"""


class Student:
    """a class representing a student
    Args:
        first_name: student first name
        last_name: student last name
        age: student age
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance
        Args:
            attrs: attribute
        """
        if (type(attrs) == list and
                all(type(eleme) == str for eleme in attrs)):
            return {m: getattr(self, m) for m in attrs if hasattr(self, m)}
        return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance
        Args:
            json: is a key value pair
        """
        for A, B in json.items():
            setattr(self, A, B)
