"""Math functions for calculator."""


def add(input_list):
    """Return the sum of the all inputs."""

    return sum(input_list)


def subtract(input_list):
    """Return all numbers subtracted from the first."""

    return input_list[0] - sum(input_list[1:])


def multiply(input_list):
    """Multiply all the inputs together."""
    total = 1
    for item in input_list:
        total *= item
    return total


def divide(input_list):
    """Divide the first input by the rest and return the result."""
    #further work - don't allow any inputs but the first to be zero
    #(ZeroDivisionError)
    divide = input_list[0]
    for num in input_list[1:]:
        divide /= num
    return divide


def square(input_list):
    """Return the sum of squares of the input."""
    total = 0
    for item in input_list:
        total += item ** 2
    return total


def cube(input_list):
    """Return the sum of cubes of the input."""
    total = 0
    for item in input_list:
        total += item ** 3
    return total


def power(input_list):
    """Raise num1 to the power of all the others and return the value."""
    power = input_list[0]
    for num in input_list[1:]:
        power **= num
    return power


def mod(input_list):
    """Return the remainder of num1 / all the other remainders."""
    mod = input_list[0]
    for num in input_list[1:]:
        mod %= num
    return mod


#not using in calc_2 exercise
# def add_mult(num1, num2, num3):
#     """Adds first 2 numbers, multiplies result by third number."""

#     return (num1 + num2) * num3

# def add_cubes(num1, num2):
#     """Adds cubes of two numbers"""

#     return (num1 ** 3) + (num2 ** 3)
