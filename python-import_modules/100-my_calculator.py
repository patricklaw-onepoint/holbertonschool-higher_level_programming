#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
}


def calculator(argv):
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    op = argv[2]

    if op in operations:
        a = int(argv[1])
        b = int(argv[3])
        print(f"{a} {op} {b} = {operations[op](a, b)}")
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)


if __name__ == "__main__":
    import sys

    calculator(sys.argv)
