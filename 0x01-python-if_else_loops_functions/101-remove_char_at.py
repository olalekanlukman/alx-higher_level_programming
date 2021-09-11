#!/usr/bin/python3

def remove_char_at(str, n):
    cstr = ""
    for m in range(len(str)):
        if m != n:
            cstr += str[m]
    return cstr
