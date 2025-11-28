#!/usr/bin/python3
"""writing to a file"""


def write_file(filename="", text=""):
    """writes to a file"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)



