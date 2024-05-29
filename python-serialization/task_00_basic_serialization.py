#!/usr/bin/env python3
"""
    Create a basic serialization module that adds
    the functionality to serialize a Python dictionary
    to a JSON file and deserialize the JSON file to
    recreate the Python Dictionary
"""
import json


def serialize_and_save_to_file(data, filename):
    """
        funtion serialize and save to file
    """
    with open(filename, 'a+') as new_file:
        add_file =   json.dump(data, new_file)
    return add_file

def load_and_deserialize(filename):
    """
        load and deserialize
    """
    with open(filename, 'r') as file_deserialize:
        load_file = json.load(file_deserialize)
    return load_file
