#!/usr/bin/env python3
"""
    funtion convert_csv_to_json
"""
import csv, json


def convert_csv_to_json(filename_csv):
    """
        convert csv to json
    """
    data = []

    try:
        with open(filename_csv, 'r', encoding='utf-8') as csvf:
            cvsReader = csv.DictReader(csvf)

            for rows in cvsReader:
                data.append(rows)

        with open("data.json", 'w', encoding='utf-8') as json_file:
            json_file.write(json.dumps(data, indent=4))

        return True
    
    except FileNotFoundError:
        print("{} file not found".format(filename_csv))
        return False
