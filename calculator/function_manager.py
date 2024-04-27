#function_manager.py

import re
import constants
import scientific
import complex_numbers
function_pattern = r'[a-zA-Z_]\w*'
constant_pattern = r'PI|EULER'

FUNCTIONS = {
    "PI": constants.PI,
    "EULER": constants.E,

    "sin": scientific.sin,
    "cos": scientific.cos,
    "log": scientific.log,

    "mean": complex_numbers.add_complex,
    "median": complex_numbers.subtract_complex,

    "add_complex": complex_numbers.add_complex,
    "subtract_complex": complex_numbers.subtract_complex

}

def get_function(name):
    return FUNCTIONS.get(name)

def get_expression():
    expression = input(':')
    while not expression:
        expression = input(':')
    return expression

def tokenize(expression):
    return re.findall(r'\d+|\.\d+|[-+*/()]|{}|{}'.format(function_pattern, constant_pattern), expression)

def is_number(token):
    return re.match(r'\d+(\.\d+)?', token)

def precedence(operator):
    if operator in ['+', '-']:
        return 1
    elif operator in ['*', '/']:
        return 2
    else:
        return 0

def apply_operator(operator, operand1, operand2):
    if operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    elif operator == '*':
        return operand1 * operand2
    elif operator == '/':
        if operand2 == 0:
            raise ValueError("Division by zero")
        return operand1 / operand2