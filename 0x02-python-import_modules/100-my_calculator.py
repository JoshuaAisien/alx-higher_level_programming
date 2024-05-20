#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div
if len(argv) == 4:
    a = int(argv[1])
    b = int(argv[3])
    operators = argv[2]

    if argv[2] == "+":
        print(f"{a} {operators} {b} = {add(a, b)} ")

    elif argv[2] == "-":
        print(f"{a} {operators} {b} = {sub(a, b)} ")

    elif argv[2] == "*":
        print(f"{a} {operators} {b} = {mul(a, b)} ")

    elif argv[2] == "/":
        print(f"{a} {operators} {b} = {div(a, b)} ")

    else:
        print("unknown operator. Available operators: +, -, * and /n")
        exit(1)
else:
    print(f"usage: {argv[0]} <a> <operator> <b> ")
    exit(1)
