#!/usr/bin/env python3
"""
    class CustomObject
"""
import pickle


class CustomObject:
    """
        class CustomObject
    """
    def __init__(self, name, age, is_student):
        """
            __init__

            args:
                name (a string)
                age (an integer)
                is_student (a boolean)
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def serialize(self, filename):
        """
            serialize the current instance of the object
            and save it to the provided filename.

            args:
                filename
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except (IOError, pickle.PickleError) as e:
            print(f"Error serializing object: {e}")
            return None

    @classmethod
    def deserialize(cls, filename):
        """
            load and return an instance of the
            CustomObject from the provided filename

            arg:
                filename
        """
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except (IOError, pickle.PickleError) as e:
            print(f"Error serializing object: {e}")
            return None

    def display(self):
        """
            method to print out the object-s
            attributes with the following format:

            Name: John
            Age: 25
            Is Student: True
        """
        print("Name: {}\nAge: {}\nIs Student: {}".format(
            self.name, self.age, self.is_student))
