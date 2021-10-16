#!/usr/bin/python3
# 4-square.py
# Lukman Mohammed
class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """Initializes the data.
        
        Args:
            size (int): size oof the square
        """
        self.__size = size

    @property
    def size(self):
        """Retrieves the size."""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2
