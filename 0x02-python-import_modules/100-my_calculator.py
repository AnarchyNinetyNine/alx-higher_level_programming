#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, mul, div, sub

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a, b = int(sys.argv[1]), int(sys.argv[3])
    operators = ["+", "-", "*", "/"]

    if sys.argv[2] not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    operations = [add(a, b), sub(a, b), mul(a, b), div(a, b)]

    for index, item in enumerate(operators):
        if sys.argv[2] == item:
            print("{} {} {} = {}".format(a, item, b, operations[index]))
