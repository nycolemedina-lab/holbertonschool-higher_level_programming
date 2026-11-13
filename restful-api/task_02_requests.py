#!/usr/bin/python3
"""
This module defines functions to fetch posts from JSONPlaceholder,
print their titles, and save them to a CSV file.
"""
import csv
import requests


def fetch_and_print_posts():
    """Fetches posts from JSONPlaceholder and prints their status and titles."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post.get("title"))


def fetch_and_save_posts():
    """Fetches posts from JSONPlaceholder and saves them to posts.csv."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()
        fieldnames = ["id", "title", "body"]

        with open("posts.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(
                f, fieldnames=fieldnames, extrasaction="ignore"
            )
            writer.writeheader()
            writer.writerows(posts)
