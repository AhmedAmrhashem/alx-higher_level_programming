#!usr/bin/python3
# 3-square.py done by Ahmed Amr
"""adding area"""

class Square:
    """calculating area methods"""

    def __init__(self, size=0):
        """constructor of class"""
        if (type(size) != int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
    
    def area(self):
        """calculate the area of the square"""
        return(self.__size**2)
