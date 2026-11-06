#!/usr/bin/python3
"""
Script that adds all command-line arguments to a Python list,
and then saves them to a JSON file ('add_item.json').
"""
import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file



def main():
    """Main execution function."""

    filename = "add_item.json"

    if os.path.exists(filename):
        items = load_from_json_file(filename)
    else:
        items = []

    items.extend(sys.argv[1:])

    save_to_json_file(items, filename)

if __name__ == "__main__":
    main()
