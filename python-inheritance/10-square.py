#!/usr/bin/python3
"""A Square class"""


Rectangle = __import__('9-rectangle.py').Rectangle


class Square(Rectangle):
    """class square"""

    def __init__(self, size):
        """init"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """area"""
        return self.__size * self.__size
