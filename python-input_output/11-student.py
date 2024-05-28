#!/usr/bin/python3
"""
    Class Student
"""


class Student:
    def __init__(self, first_name, last_name, age):
        """
            constructor method
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None):
        """
            retrieves a dictionary representation
            of a Student instance

            If attrs is a list of strings, only attribute names
            contained in this list must be retrieved.

            Otherwise, all attributes must be retrieved
        """
        if attr is not None:
            return {attrs: getattr(self, attrs) for attrs in attr
                    if hasattr(self, attrs)}
        return self.__dict__

    def reload_from_json(self, json):
        """
            method replaces all attributes of the Student instance
        """
        for key, value in json.items():
            setattr(self, key, value)
