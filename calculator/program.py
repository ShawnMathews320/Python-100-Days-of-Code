from unittest import result
from art import logo

import operator

def performMath(number1, operation, number2):  # does our calculator math
    # convert string operators to real operators with dictionary
    ops = { '+': operator.iadd,
            "-": operator.isub, 
            '*': operator.imul, 
            '/': operator.truediv
        }  

    result = ops[operation](number1, number2)  # result after operations
    continueMath = input(f"Type 'y' to continue calculating with {result}, or type 'n' to exit: ")

    if continueMath == 'n':
        print(f"{number1} {operation} {number2} = {result}")  # show results to user
    else:
        operation = input("Pick an operation (i.e. +, -, *, /): ")
        secondNumber = float(input("What is the next number?: "))
        performMath(result, operation, secondNumber)

print(logo)

firstNumber = float(input("What is the first number?: "))
operation = input("Pick an operation (i.e. +, -, *, /): ")
secondNumber = float(input("What is the next number?: "))

performMath(firstNumber, operation, secondNumber)  # give function inputs