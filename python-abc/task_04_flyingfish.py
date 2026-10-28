#!/usr/bin/env python3
"""
Module demonstrating multiple inheritance and Method Resolution Order (MRO)
using Fish, Bird, and FlyingFish classes.
"""


class Fish:
    """Class representing a fish."""

    def swim(self):
        """Prints swimming behavior for a fish."""
        print("The fish is swimming")

    def habitat(self):
        """Prints habitat for a fish."""
        print("The fish lives in water")


class Bird:
    """Class representing a bird."""

    def fly(self):
        """Prints flying behavior for a bird."""
        print("The bird is flying")

    def habitat(self):
        """Prints habitat for a bird."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Class representing a flying fish, inheriting from Fish and Bird."""

    def fly(self):
        """Overrides fly method for flying fish."""
        print("The flying fish is soaring!")

    def swim(self):
        """Overrides swim method for flying fish."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Overrides habitat method for flying fish."""
        print("The flying fish lives both in water and the sky!")


# --- Testing and MRO Exploration ---
if __name__ == "__main__":
    # Instantiate FlyingFish
    flying_fish = FlyingFish()

    # Call overridden methods
    flying_fish.fly()
    flying_fish.swim()
    flying_fish.habitat()

    print("\n--- Method Resolution Order (MRO) ---")
    print(FlyingFish.mro())
