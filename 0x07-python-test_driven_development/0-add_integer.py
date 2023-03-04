#!/usr/bin/python3
"""
    function to add to int or floats. casts floats to int
"""


def add_integer(a, b=98):
    ''' b is 98 by default '''
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:	
        return int(a) + int(b)
