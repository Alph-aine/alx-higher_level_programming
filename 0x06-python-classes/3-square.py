#!/usr/bin/python3
"""Create a  class"""


class Square:
    """ This class has a private instance"""
    def __init__(self, size=0):
        """ This is a initializing function.
        It checks if the size passed is an integer and also > 0
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self._size = size

    def area(self):
        """ Returns the area of the current square """
        return (self._size ** 2)
