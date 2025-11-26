#!/usr/bin/python3
"""define base geometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """rectangle"""

    def __init__(self, width, height):
        """init"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Return rectangle description"""
        return f"[Rectangle] {self.__width}/{self.__height}"
