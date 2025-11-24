#!/usr/bin/python3
class MyList(list):
    """A list subclass with a method to print a sorted version."""

    def print_sorted(self):
        """Print the list in ascending order without modifying the original list."""
        print(sorted(self))

