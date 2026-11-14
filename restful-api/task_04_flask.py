#!/usr/bin/python3
"""
A simple RESTful API built with Flask supporting GET and POST endpoints
for managing an in-memory dictionary of users.
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for users (keep empty for checker compatibility)
users = {}


@app.route("/")
def home():
    """Return a welcome message at the root URL."""
    return "Welcome to the Flask API!"


@app.route("/data")
def get_data():
    """Return a JSON list of all stored usernames."""
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    """Return API status confirmation."""
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """Return the full user object for a given username, or 404 if missing."""
    user = users.get(username)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)


@app.route("/add_user", methods=["POST"])
def add_user():
    """Add a new user from JSON request payload with input validation."""
    data = request.get_json(silent=True)

    if data is None or not isinstance(data, dict):
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = data
    return jsonify({
        "message": "User added",
        "user": data
    }), 201


if __name__ == "__main__":
    app.run()
