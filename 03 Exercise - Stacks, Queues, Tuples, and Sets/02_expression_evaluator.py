from functools import reduce

expression = input().split()

inx = 0

functions = {
    "*": lambda i: reduce(lambda a, b: int(a) * int(b), expression[:i]),
    "/": lambda i: reduce(lambda a, b: int(a) / int(b), expression[:i]),
    "+": lambda i: reduce(lambda a, b: int(a) + int(b), expression[:i]),
    "-": lambda i: reduce(lambda a, b: int(a) - int(b), expression[:i])
}

while inx < len(expression):
    element = expression[inx]

    if element in "+-*/":
        result = functions[element](inx)
        [expression.pop(1) for i in range(inx)]
        expression[0] = result
        inx = 0

    inx += 1

print(int(expression[0]))
