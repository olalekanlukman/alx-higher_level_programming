#!/usr/bin/python3


def delete_at(my_list=[], idx=0):
    if my_list:
        if len(my_list) <= idx or idx < 0:
            return my_list
        else:
            del my_list[idx]
        return my_list
