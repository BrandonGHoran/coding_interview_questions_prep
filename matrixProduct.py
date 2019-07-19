#! /usr/bin/env python

#moving only down and right, find the maximum product in a 2d array

import numpy as np

def prod(m):
    p=np.zeros(shape=(len(m),len(m[0])))

    p[0][0] = m[0][0]

    for i in range(1, len(p)):
        p[0][i] = p[0][i-1]*m[0][i]
    for i in range(1, len(p[0])):
        p[i][0] = p[i-1][0]*m[i][0]
    
    for i in range(1, len(p)):
        for j in range(1, len(p[0])):
            p[i][j] = m[i][j]*max(p[i-1][j], p[i][j-1])#the best you can do is the best of either above or left

    print(p)
    print(p[-1][-1])

