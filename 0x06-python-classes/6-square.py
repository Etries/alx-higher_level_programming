#!/usr/bin/python3
""" class Square that defines a square"""


class Square:
    """ class Square that defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        """ init size of the square."""
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
        if type(position) is tuple and len(position) == 2:
            self.__position = position
        else:
            raise TypeError("size must be an integer")

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

    @property
    def position(self):
        """ private position"""
        return self.__position

    @position.setter
    def position(self, position):
        """sets position"""
        if type(position) is tuple and len(position) == 2:
            self.__position = position
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """returns the area"""
        return self.__size**2

    def my_print(self):
        """ prints sqaur with # """
        if self.__size == 0:
            print()
        else:
            for x in range(self.__size):
                if self.__position[0] > 0:
                    for x in range(self.__position[0]):
                        print(" ", end= "")
                for y in range(self.__size):
                    print("#", end="")
                print()
