from functools import reduce


def operate(operator, *data):
    def addition(a, b):
        return a + b

    def subtraction(a, b):
        return a - b

    def multiplication(a, b):
        return a * b

    def division(a, b):
        if a != 0:
            return a / b

    if operator == '+':
        return reduce(addition, data)

    elif operator == '-':
        return reduce(subtraction, data)

    elif operator == '*':
        return reduce(multiplication, data)

    elif operator == '/':
        return reduce(division, data)


print(operate("+", 1, 2, 3))
