#!/usr/bin/python3
"""
This module defines "fetch_and_print_posts" that  post from JSONPlaceholder.
and "fetch_and_save_posts" that
"""
import requests
import csv
import json

def fetch_and_print_posts()
    """func"""
    r = requests.get("https://jsonplaceholder.typicode.com")
    r.status_code
    r.json()
    print("tiles")

def fetch_and_save_posts()
    """func"""
    data = requests.get("https://jsonplaceholder.typicode.com")
    data_list = ["id": "id_v", "title": "titles_v", "body": "body_v"]
    with open("data", "w", newline="", encode="utf-8") as f:
        wwriter = csv.DictWriter(f, data_list=data_list)
        writer.writeheader()
        writer.writerows(records)
