#!/usr/bin/python3
"""Create a  class"""


class Square:
    """ This class has a private instance"""
    def __init__(self, size=0, position=(0, 0)):
        """ This is a initializing function.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """this getter returns the position"""
        return self.__position

    @position.setter
    def position(self, value):
        """ position's setter"""
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or type(value[1]) is not int or \
           value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """ Returns the area of the current square """
        return (self.__size ** 2)

    def my_print(self):
        """This method prints the square"""
        if self.__size <= 0:
            print()
        for i in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size, end='')
            print()
