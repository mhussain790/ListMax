"""
Name: Masud Hussain
Course: CS162
Assignment: 6A
"""

"""
Write a recursive function named list_max that takes as its parameter 
a list of numbers and returns the maximum value in the list. 
You can assume the list contains at least one element. 
If multiple elements of the list are tied for the maximum, 
you would still return that value.

You cannot call the built-in max() function.

You may use default arguments and/or helper functions.

Your recursive function must not:

use any loops
use any variables declared outside of the function
use any mutable default arguments
The file must be named: list_max.py
"""


def list_max(a_list):

    if len(a_list) == 1:
        return a_list[0]

    if a_list[0] > a_list[1]:
        a_list.pop(1)
    else:
        a_list.pop(0)
    return list_max(a_list)
