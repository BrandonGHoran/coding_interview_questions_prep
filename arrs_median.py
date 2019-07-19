#! /usr/bin/env python

import math

#given 2 arrays, finds the median of the two arrays
#this way is slightly ineffective in memeory because it creates a new array
#in terms of time complexity, it is still linear, so that's pretty good
def median(a1,a2):
    #combine arrays then find median
    p1=0
    p2=0
    a=[]
    while p1 < len(a1) and p2 < len(a2):
        if a1[p1] < a2[p2]:
            a.append(a1[p1])
            p1+=1
        else:
            a.append(a2[p2])
            p2+=1

    if p1 == len(a1):
        for i in range(p2, len(a2)):
            a.append(a2[i])
    else:
        for i in range(p1, len(a1)):
            a.append(a1[i])

    mid = len(a)//2
    if len(a)%2==0:
        return (a[mid]+a[mid-1])/2
    else:
        return a[mid]
