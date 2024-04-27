#evaluator.py

from function_manager import apply_operator

def evaluate_expression(parsed_expression):
    operand_stack = []

    for token in parsed_expression:
        if isinstance(token, (int, float, complex)):
            operand_stack.append(token)
        else:
            operand2 = operand_stack.pop()
            operand1 = operand_stack.pop()
            result = apply_operator(token, operand1, operand2)
            operand_stack.append(result)

    return operand_stack.pop()
