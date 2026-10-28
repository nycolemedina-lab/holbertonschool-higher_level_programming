#!/usr/bin/env python3
"""
Module demonstrating mixin classes in Python by equipping a Dragon class
with swimming and flying capabilities.
"""


class SwimMixin:
    """Mixin class providing swimming capability."""

    def swim(self):
        """Prints swimming behavior."""
        print("The creature swims!")


class FlyMixin:
    """Mixin class providing flying capability."""

    def fly(self):
        """Prints flying behavior."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class inheriting abilities from SwimMixin and FlyMixin."""

    def roar(self):
        """Prints dragon roaring behavior."""
        print("The dragon roars!")


# --- Testing the Dragon's Abilities ---
if __name__ == "__main__":
    draco = Dragon()

    draco.swim()
    draco.fly()
    draco.roar()
