#!/usr/bin/python3


def uniq_add(my_list=[]):
    s = set(my_list)
    sum = 0
    for x in s:
        sum += x
    return sum
