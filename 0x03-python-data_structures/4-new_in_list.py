#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    if my_list:
        x = []
        for i in my_list:
            if i != my_list[idx]:
                x.append(i)
            else:
                x[idx] = element
        return x
