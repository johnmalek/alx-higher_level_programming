#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    arguments = sys.argv
    no_of_args = len(arguments)

    if no_of_args != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    operator_1 = int(arguments[1])
    operator_2 = int(arguments[3])
    operand = arguments[2]

    operators = ["+", "-", "*", "/"]

    if operand not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    else:
        if operand == "+":
            result = add(operator_1, operator_2)
            print("{} + {} = {}".format(operator_1, operator_2, result))
        elif operand == "-":
            result = sub(operator_1, operator_2)
            print("{} - {} = {}".format(operator_1, operator_2, result))
        elif operand == "*":
            result = mul(operator_1, operator_2)
            print("{} * {} = {}".format(operator_1, operator_2, result))
        else:
            result = div(operator_1, operator_2)
            print("{} / {} = {}".format(operator_1, operator_2, result))
