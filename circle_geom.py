#! /usr/bin/env python

#determines, for 2 circles, given by their center and radius, what state they are in:
#
#tangent
#overlapping
#concentric
#equal
#disjoint (inside)
#disjoint (outside)

import matplotlib.pyplot as plt

def state(x1,y1,r1,x2,y2,r2):
    if x1==x2 and y1==y2:
        if r1 == r2:
            return "equal"
        else:
            return "concentric"

    x1Min = x1-r1
    x1Max = x1+r1
    x2Min = x2-r2
    x2Max = x2+r2
    y1Min = y1-r1
    y1Max = y1+r1
    y2Min = y2-r2
    y2Max = y2+r2
    centerDist = ((x1-x2)**2+(y1-y2)**2)**0.5

    #print("centerDist=" + str(centerDist))

    if r1 + r2 < centerDist:
        return "disjoint (outside)"
    elif r1 + r2 == centerDist:
        return "touching"

    if (x1Min<x2Min and x1Max>x2Max and y1Min<y2Min and y1Max>y2Max) or (x2Min<x1Min and x2Max>x1Max and y2Min<y1Min and y2Max>y1Max):
        return "disjoint (inside)"
    else:
        return "overlapping"


def plotCircles(x1,y1,r1,x2,y2,r2):
    ax=plt.gca()
    ax.add_patch(plt.Circle((x1,y1),radius=r1))
    ax.add_patch(plt.Circle((x2,y2),radius=r2))
    plt.axis('scaled')
    plt.show()


def circles(x1,y1,r1,x2,y2,r2):
    print(state(x1,y1,r1,x2,y2,r2))
    plotCircles(x1,y1,r1,x2,y2,r2)

