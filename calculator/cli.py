from parser import parse_expression # type: ignore
from evaluator import evaluate_expression
from function_manager import get_expression


def main():

    expression = get_expression()
    parsed_expression = parse_expression(expression)
    result = evaluate_expression(parsed_expression)
    print("Result:", result)

if __name__ == '__main__':
    main()