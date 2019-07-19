#! /usr/bin/env python

import math

def binary(n):

    if n < 2:
        return str(n)

    if n%2==0:#it's even, the last digit is 0
        return binary3(n//2) + "0"
    else:
        return binary3(n//2) + "1"

