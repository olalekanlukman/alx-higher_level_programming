#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    if my_list:
        x = []
        for i in my_list:
            x.append(i)
        x[idx] = element
        return x
