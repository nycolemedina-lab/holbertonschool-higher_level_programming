#!/usr/bin/python3
"""
This module provides a function to convert CSV file contents
into a JSON file format using DictReader.
"""
import csv
import json


    def convert_csv_to_json(csvfile):
        """Convert a csv file into a json file.
        Args:
            csvfile: csv file to convert to json.
        Returns:
            bool: True if conversion succeeds, Fales otherwise.
        """
        try:
            with open(csvfile, "r", encoding="utf-8") as csvf:
                data = list(csv.DictReader(csvf))

            with open("data.json", "w", encoding="utf-8") as jf:
                json.dump(data, jf, indent=4)
            return True

        except Excption:
            return False
