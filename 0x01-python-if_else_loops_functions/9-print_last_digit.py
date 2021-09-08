#!/usr/bin/python3
# 9-print_last_digit.py
# Lukman Mohammed


def print_last_digit(number):
    """Print the last digit of a number and returns it"""
    x = abs(number) % 10
    print("{}".format(x), end="")
    return (x)
