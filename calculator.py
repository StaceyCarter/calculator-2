"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *

# def token_string(sen):
#     """ tokenizing the input"""
#     tokens = sen.split(" ")
#     return tokens

def run_calculator():

    while True:
        user_input = input("")

        tokens = user_input.split(" ")
        if tokens[0] == "q":
            break
        elif tokens[0] == "+":
            print(add(float(tokens[1]), float(tokens[2])))
        elif tokens[0] == "-":
            print(subtract(float(tokens[1]), float(tokens[2])))
        elif tokens[0] == "*":
            print(multiply(float(tokens[1]), float(tokens[2])))
        elif tokens[0] == "/":
            print(divide(float(tokens[1]), float(tokens[2])))
        elif tokens[0] == "square":
            print(square(float(tokens[1])))
        elif tokens[0] == "cube":
            print(cube(float(tokens[1])))
        elif tokens[0] == "pow":
            print(power(float(tokens[1]), float(tokens[2])))
        elif tokens[0] == "mod":
            print(mod(float(tokens[1]), float(tokens[2])))
            


run_calculator()

# while True:
    

# Your code goes here
