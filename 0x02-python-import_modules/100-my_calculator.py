#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import *
    import sys
    size = len(sys.argv) - 1
    if size < 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    operators = ["+", "-", "*", "/"]
    sign = sys.argv[2]
    if sign not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    elif sign in operators:
        if sign == "+":
            print("{} + {} = {}".format(a, b, add(a, b)))
        elif sign == "-":
            print("{} - {} = {}".format(a, b, sub(a, b)))
        elif sign == "*":
            print("{} * {} = {}".format(a, b, mul(a, b)))
        elif sign == "/":
            print("{} / {} = {}".format(a, b, div(a, b)))
