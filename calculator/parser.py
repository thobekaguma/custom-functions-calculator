#parser.py

from function_manager import *

def parse_expression(expression):
    tokens = tokenize(expression)
    parsed_expression = []
    operator_stack = []

    for token in tokens:
        if is_number(token):
            parsed_expression.append(float(token))
        elif token in ['+', '-', '*', '/']:
            while operator_stack and precedence(operator_stack[-1]) >= precedence(token):
                parsed_expression.append(operator_stack.pop())
            operator_stack.append(token)
        elif token == '(':
            operator_stack.append(token)
        elif token == ')':
            while operator_stack and operator_stack[-1] != '(':
                parsed_expression.append(operator_stack.pop())
            operator_stack.pop()  # Discard the '('
        else:
            raise ValueError("Invalid token: {}".format(token))

    while operator_stack:
        parsed_expression.append(operator_stack.pop())

    return parsed_expression

