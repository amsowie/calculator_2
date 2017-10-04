"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic_2 import *


# Your code goes here
def input_calc():
    """Get calculator input and put into list

    Prompts the user to enter some input,
    and split out results into a list"""
    calc_input = raw_input("> ").split()
    return calc_input


def convert_nums_to_float(input_list):
    """convert numbers to float from string format

    Takes index 1 on and converts all to floats, leaves index 0 as string"""
    float_list = [input_list[0]]

    for item in input_list[1:]:
        try:
            float_list.append(float(item))
        except ValueError:
            print "Enter an operator followed by numbers separated by spaces."
            print "Do not enter any non-numbers after the operator."
            return None

    return float_list


def which_calc_type(input_list):
    """Determines calculation type based on first index

    Compares each first index of user input string to
    computation symbols and calls proper calculation function"""

    # in progress - left off
    # print len(input_list)
    # if input_list[0] == "square" or input_list[0] == "cube":
    #     if len(input_list) < 2:
    #         "You did not enter in enough arguments"
    #         answer = None

    input_list = convert_nums_to_float(input_list)
    if input_list is None:
        answer = None
    elif input_list[0] == "+":
        answer = add(input_list[1:])
    elif input_list[0] == "-":
        answer = subtract(input_list[1:])
    elif input_list[0] == "*":
        answer = multiply(input_list[1:])
    elif input_list[0] == "/":
        answer = divide(input_list[1:])
    elif input_list[0] == "square":
        answer = square(input_list[1:])
    elif input_list[0] == "cube":
        answer = cube(input_list[1:])
    elif input_list[0] == "pow":
        answer = power(input_list[1:])
    elif input_list[0] == "mod":
        answer = mod(input_list[1:])
    elif input_list[0].lower() == "q" or input_list[0].lower() == "quit":
        answer = None
    else:
        print "Enter an operator followed by numbers separated by spaces."
        print "You did not enter a valid operator."
        answer = None

    return answer


while True:
    calc_list = input_calc()
    calc_answer = which_calc_type(calc_list)
    if calc_answer is None:
        break
    print calc_answer
