#!/usr/bin/python3


def multiply_list_map(my_list=[], number=0):
    x = list(map(lambda my: number * my, my_list))
    return x
