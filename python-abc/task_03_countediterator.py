#!/usr/bin/python3
"""
Module containing CountedIterator class that tracks the number of items
fetched during iteration.
"""


class CountedIterator:
    """An iterator wrapper that keeps track of the number of iterated items."""

    def __init__(self, iterable):
        """Initializes the iterator object and counter."""
        self.__iterator = iter(iterable)
        self.__count = 0

    def get_count(self):
        """Returns the current number of items that have been fetched."""
        return self.__count

    def __iter__(self):
        """Returns the iterator object itself."""
        return self

    def __next__(self):
        """
        Increments the counter and fetches the next item.
        Raises StopIteration when no items are left.
        """
        item = next(self.__iterator)
        self.__count += 1
        return item


# --- Testing ---
if __name__ == "__main__":
    items = ["apple", "banana", "cherry", "date"]
    counted_iter = CountedIterator(items)

    # Manual iteration calls
    print(f"Fetched: {next(counted_iter)}")
    print(f"Fetched: {next(counted_iter)}")
    print(f"Current Count: {counted_iter.get_count()}")

    # Loop iteration over remaining items
    for item in counted_iter:
        print(f"Loop Fetched: {item}")

    print(f"Final Count: {counted_iter.get_count()}")
