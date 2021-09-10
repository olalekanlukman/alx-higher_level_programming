#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    boo = []

    for ele in my_list:
        if ele % 2 == 0:
            boo.append(True)
        else:
            boo.append(False)
    return boo
