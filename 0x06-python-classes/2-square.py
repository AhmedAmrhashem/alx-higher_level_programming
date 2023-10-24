#!usr/bin/python3
# 2-square.py done by Ahmed Amr
"""Validations"""

class Square:
    """validations and checks"""

    def __init__(self, size=0):
        """constructor of class"""
        if (type(size) != int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size 

