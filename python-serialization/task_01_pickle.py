#!/usr/bin/python3
"""
This module defines the CustomObject class with
pickle-based serialization and deserialization methods.
"""
import pickle


class CustomObject:
    """Represent a custom object with serialization
    capabilities."""

    def __init__(self, name, age, is_student):
        """Initialize a new CustomObject instance.

        Args:
            name (str): Name of the object owner.
            age (int): Age of the object owner.
            is_student (bool): Student status.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """prints out the object's attributes"""
        print(f"Name: {self.name}\nAge: {self.age}\n"
              f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """serialize the current instance of the object
        and save it to the provided filename."""
        with open(filename, "wb") as f:
            pickle.dump(self, f)

    @classmethod
    def deserialize(cls, filename):
        """load and return an instance of the CustomObject
        from the provided filename."""
        with open(filename, "rb") as f:
            return pickle.load(f)
