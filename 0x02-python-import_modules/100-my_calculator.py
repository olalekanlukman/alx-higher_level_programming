#!/usr/bin/python3


if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

if len(sys.argv) != 4:
    print("usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)

operators = ['+', '-', '*', '/']
math = [add, sub, mul, div]
for i in range(0, 4):
    if sys.argv[2] == operators[i]:
        print("{} {} {} = {}".format(sys.argv[1], operators[i], sys.argv[3],
              mul(int(sys.argv[1]), int(sys.argv[3]))))
        break

if sys.argv[2] != operators[i]:
    print("Unknown operator. Available operators: +, -, * and /")
