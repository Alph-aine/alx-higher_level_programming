#!/usr/bin/python3
"""Create a  class"""


class Square:
    """ This class has a private instance"""
    def __init__(self, size=0):
        """ This is a initializing function.
        """
        self.__size = size

    @property
    def size(self):
        """ A getter """
        return self.__size

    @size.setter
    def size(self, value):
        """A setter"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Returns the area of the current square """
        return (self.__size ** 2)

    def my_print(self):
        """This method prints the square"""
        if self.__size <= 0:
            print()
        for i in range(self.__size):
            print("#" * self.__size, end='')
            print()
