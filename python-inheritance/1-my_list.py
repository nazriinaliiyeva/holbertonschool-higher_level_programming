#!/usr/bin/python3
"""doc"""


class MyList(list):
    """A list subclass with a method to print a sorted version."""

    def print_sorted(self):
        """Print the list in ascending order"""
        print(sorted(self))
