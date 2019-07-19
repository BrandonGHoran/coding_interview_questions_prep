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

#this version is slightly cleaner
def k2(ws, vs, c):
    n=len(ws)
    k=np.zeros(shape=(n,c+1))

    for i in range(0, n):#for each item
        for w in range(1, c+1):#for each total weight possible in the bag
            if w < ws[i]:#if this item can't be added to the bag
                k[i][w] = k[i-1][w]#the best we can do is as good as we could do for this weight without this item
            else:#we can include this item
                #the best we can do is the maximum of either including this item or not
                k[i][w] = max(vs[i]+k[i-1][w-ws[i]],k[i-1][w])#the best is either the value of this item plus the best we could do with one less item and weight - weight of current item OR just not choosing this item

    return k[n-1][c]


