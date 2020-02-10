from math import sin, cos, log, tan, sqrt


def evaluate_expression(expression):
    return eval(expression)


if __name__ == "__main__":
    while True:
        print(evaluate_expression(input()))
