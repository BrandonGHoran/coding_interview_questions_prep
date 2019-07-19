#! /usr/bin/env python

#calculates the first n fibbonacci numbers

fibs=[0, 1]
#calcs first n fib numbers
def fib(n):
    if n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        return fib2(n)

def fib2(n):
    for i in range(2, n):
        fibs.append(fibs[i-1]+fibs[i-2])
    return fibs


