#!/usr/bin/python3
"""
This module defines an abtract class 'Animal' with subclass 'cat' and 'dog'
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract class animal"""

    @abstractmethod
    def sound(self):
        """sound the animal makes"""
        ...

class Dog(Animal):
    """dog class"""

    def sound(self):
        """sound of the dog"""
        return "Bark"

class Cat(Animal):
    """cat class"""

    def sound(self):
        """sound of cat"""
        return "Meow"
