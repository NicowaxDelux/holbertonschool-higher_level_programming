#!/usr/bin/python3
"""
    method load from json file
"""
import json


def load_from_json_file(filename):
    """
        function that creates an Object from a “JSON file”
    """
    with open(filename, encoding="utf-8") as load_file:
        return json.load(load_file)
