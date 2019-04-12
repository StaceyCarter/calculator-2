"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic2 import *
from functools import reduce

# def token_string(sen):
#     """ tokenizing the input"""
#     tokens = sen.split(" ")
#     return tokens

def run_calculator():

    while True:
        user_input = input("> ")

        tokens = user_input.split(" ")
        operator = tokens[0]


        if operator == "q":
            break

        numbers = convert_nums_to_floats(tokens[1:])


        if operator == "+":
            print(add(numbers))
        elif operator == "-":
            print(subtract(numbers))
        elif operator == "*":
            print(multiply(numbers))
        elif operator == "/":
            print(divide(numbers))
        elif operator == "pow":
            print(power(numbers))
        elif operator == "mod":
            print(mod(numbers))

        if len(numbers) == 1 and operator == "square":
            print(square(numbers[0]))
        
        if len(numbers) == 1 and operator == "cube":
            print(cube(numbers[0]))

        if len(numbers) > 1 and operator == "square" or operator == "cube":
            print("Too many numbers for this function")
            run_calculator()

            

def convert_nums_to_floats(li):
    """List -> List. Takes in tokenized input and converts everything into floats
    """
    floatified = []
    for number in li:
        floatified.append(float(number))
    return floatified



run_calculator()


