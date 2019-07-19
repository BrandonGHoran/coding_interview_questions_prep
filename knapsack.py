#! /usr/bin/env python

import numpy as np
#solves the knapsack problem

def knapsack(ws, vs, c): 
    n=len(ws)
    knapsack = np.zeros(shape=(n+1,c+1))

    for i in range(0, knapsack.shape[0]):
        knapsack[i][0] = 0
    for i in range(0, knapsack.shape[1]):
        knapsack[0][i] = 0

    for i in range(1, n+1): 
        for w in range(1, c+1): 
            if ws[i-1] <= w:#if this item is light enough to be in the bag 
                knapsack[i][w] = max(vs[i-1] + knapsack[i-1][w-ws[i-1]],  knapsack[i-1][w])#I should choose the best of the either adding this item or not
            else: 
                knapsack[i][w] = knapsack[i-1][w] 
  
    return knapsack[n][c] 



