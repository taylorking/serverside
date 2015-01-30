#!/usr/bin/env python3.4
def sum(*args):
    sum = 0 
    for i in range(0, len(args)):
        sum+=args[i]
    return sum
def mean(*args):
    sum = 0 
    for i in range(0, len(args)): 
        sum+=args[i]
    return sum / len(args)
def median(*args):
    args = list(args)
    args.sort()
    return args[len(args) // 2] 
print(median(5,4,3))
