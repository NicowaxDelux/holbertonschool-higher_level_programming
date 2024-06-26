#!/usr/bin/python3
"""
    script that adds all arguments to a Python list,
    and then save them to a file
"""
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

open("add_item.json", 'a')
try:
    new = load_from_json_file("add_item.json")
except ValueError:
    new = []
save_to_json_file(new + sys.argv[1:], "add_item.json")
