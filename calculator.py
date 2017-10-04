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
    return calc_input


def convert_nums_to_float(input_list):
    """convert numbers to float from string format

    Takes index 1 on and converts all to floats, leaves index 0 as string"""
    float_list = [input_list[0]]

    for item in range(1,len(input_list)):
        float_list.append(float(input_list[item]))

    return float_list


def which_calc_type(input_list):
    """Determines calculation type based on first index

    Compares each first index of user input string to
    computation symbols and calls proper calculation function"""

    input_list = convert_nums_to_float(input_list)

    if input_list[0] == "+":
        answer = add(input_list[1], input_list[2])
    elif input_list[0] == "-":
        answer = subtract(input_list[1], input_list[2]) 
    elif input_list[0] == "*":
        answer = multiply(input_list[1], input_list[2])
    elif input_list[0] == "/":
        answer = divide(input_list[1], input_list[2])
    elif input_list[0] == "square":
        answer = square(input_list[1])
    elif input_list[0] == "cube":
        answer = cube(input_list[1])
    elif input_list[0] == "pow":
        answer = power(input_list[1], input_list[2])
    elif input_list[0] == "mod":
        answer = mod(input_list[1], input_list[2])
    elif input_list[0].lower() == "q" or input_list[0].lower() == "quit":
        answer = None
    else:
        print "Entry not valid"
        answer = None

    return answer


calc_list = input_calc()

print which_calc_type(calc_list)
