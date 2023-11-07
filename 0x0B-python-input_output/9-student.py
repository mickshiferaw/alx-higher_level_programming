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

    def to_json(self):
        """method that retrieves a dictionary representation of a Student"""
        return self.__dict__
