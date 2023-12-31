#!/usr/bin/python3
""" class Square that defines a square"""


class Square:
    """ class Square that defines a square"""
    def __init__(self, size=0):
        """ init size of the square."""
        self.size = size

    @property
    def size(self):
        """int: private size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets value into size, must be int."""
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """returns the area"""
        return self.__size**2

    def my_print(self):
        """ prints sqaur with # """
        if self.__size == 0:
            print()
        else:
            for x in range(self.__size):
                for y in range(self.__size):
                    print("#", end="")
                print()
