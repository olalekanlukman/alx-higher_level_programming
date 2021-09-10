#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    x = list(tuple_a)
    y = list(tuple_b)
    
    q = []
    i = 0
    z = 2
    if len(x) < 2:
        for j in range(0, 2 - len(x)):
            x.append(0)
    if len(y) < 2:
        for k in range(0, 2 - len(y)):
            y.append(0)
    while (z > 0):
        q.append(x[i] + y[i])
        i += 1
        z -= 1
    return tuple(q)
