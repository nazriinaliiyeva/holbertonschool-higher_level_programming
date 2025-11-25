#!/usr/bin/python3
"""doc"""


def inherits_from(obj, a_class):
    """doc"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
