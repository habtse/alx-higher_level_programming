#!/usr/bin/python3
#1-rectangle.py
'''Define rectangle class'''

class Rectangle:
    '''representation of class Rectangle'''
    def __init__(self,width,height):
        ''' initializing the attribute of Rectangle
        Args: 
            width(int): the width of the new rectangle
            height(int): the height of the new rectangle
        '''
        self.__height = height
        self.__width = width

    @property
    def height(self):
        ''' get the rectangle height'''
        return self.__height

    @height.setter
    def height(self,value):
        if not isinstance(value, int):
            raise TypeError("width must be integer")
        if value < 0:
            raise ValueError("width cannot be negative")
        self.__height = value

    @property
    def width(self):
        ''' get the rectangle width'''
        return self.__width

    @width.setter
    def width(self,value):
        if not isinstance(value, int):
            raise TypeError("width must be integer")
        if value < 0:
            raise ValueError("width cannot be negative")
        self.__width = value
