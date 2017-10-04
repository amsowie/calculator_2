"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
def input_calc():
    """Get calculator input and put into list
    
    Prompts the user to enter some input, 
    and split out results into a list"""
    calc_input = []
    calc_input = raw_input("> ").split()
    print calc_input
    return None




input_calc()
