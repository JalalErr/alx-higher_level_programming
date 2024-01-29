#!/usr/bin/python3

def add_integer(a, b = 98):
    """ 
    Function add two integer numbers.

    Args: 
        a: first integer number.
        b: secound integer number.
    
    Return: 
        Sum of the two input integers.
    
    Raise: 
        TypeError if the input not an integers.
    """

    if (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError('a must be an integer')
    if (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError('b must be an integer')
