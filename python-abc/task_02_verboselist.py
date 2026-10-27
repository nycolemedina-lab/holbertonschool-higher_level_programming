#!/usr/bin/python3
"""
Module containing VerboseList class that inherits from the built-in list
and prints notifications when elements are added or removed.
"""


class VerboseList(list)
    """Custom list subclass that prints notifications when modification."""

    def append(self, item):
        """Appends item to the list and prints a notification.""""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, item):
        """Extends list with an iterable and prints a notification."""
        items = list(iterable)
        count = len(items)
        super().extend(items)
        print(f"Extended the list with [{count}] items.")

    def remove(self, item):
        """Prints a notification and removes the specified item."""
        print(f"Remove [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Prints a notification and pops an item at index (default last)."""
        items = self[index]
        print(f"popped [{item}] from the list.")
        return super().pop(index)
