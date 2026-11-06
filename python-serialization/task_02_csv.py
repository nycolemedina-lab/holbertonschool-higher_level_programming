#!/usr/bin/python3
"""

"""
import csv
import json


    def convert_csv_to_json(csvfile):
        """Convert a csv file into a json file.
        Args:
            csvfile: csv file to convert to json.
        """
        with open(csvfile, "r") as csvf:
            data = list(csv.DictReader(csvf))

        with open('data.json', "w") as jf:
            json.dump(data, jf)
