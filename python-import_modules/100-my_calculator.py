#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    if sys.argv[2] not in ("+", "-", "*", "/"):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    sys.argv[1] = a
    sys.argv[2] = op
    sys.argv[3] = b
    print("{} {} {} = {}".format(int(a), op, int(b), int(a) + int(b)))
