#! /usr/bin/env python

#determines if a number is prime

primes=[2]

def prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    d=False
    for i in range(3, n+1):
        #check if number can be decomposed into primes
        for p in primes:
            if i%p==0:#then it can be decomposed
                break
        else:
            primes.append(i)

    print(primes)

    return True if primes[-1] == n else False

