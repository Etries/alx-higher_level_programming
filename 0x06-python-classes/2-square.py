#!/usr/bin/python3
""" An square class"""


class Square:
    """ square class with attributes"""

    def __init__(self, size=0):
        """ init function """
        
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >=0")
        else:
            self.__size = size
