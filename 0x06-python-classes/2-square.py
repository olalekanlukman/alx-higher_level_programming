#!/usr/bin/python3
# 2-square.py
# Lukman Mohammed
"""Defines a class square"""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initializes the data.


        Args:
            size (int): gives the size of a square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
