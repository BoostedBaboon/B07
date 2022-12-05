## Place where all forces are calculated on each fastener
from math import *
from Variables import Fx, Fy, Fz, Mx, My, Mz


## Creating formulas/actions needed multiple times
def SumLists(list1, list2, sign):
    mainlist = []
    if sign == "-":
        for F1 in list1:
            for F2 in list2:
                mainlist.append(F1 - F2)        ##subtract each element of F2 from each element of F1
    if sign == "+":
        for F1 in list1:
            for F2 in list2:
                mainlist.append(F1 + F2)        ##add each element of F2 with each element of F1
    return mainlist

def FindAbsoluteMax(list1, list2):              ## finds the absolute maximum of the subtracktion/addition of 2 lists
    R1 = SumLists(list1, list2, "+")
    R2 = SumLists(list1, list2, "-")
    maxlist = max(max(R1, R2))
    minlist = min(min(R1, R2))
    if abs(maxlist) >= abs(minlist):
        absmax = maxlist
    else:
        absmax = minlist
    return absmax

## Multiple cases possible, 1 is a 4 fasterner config, 2 is a 6 fastener config, 3 is an 8 fastener config.
def CalculateForces(Case, rz, ry):

    r = []
    alpha = []
    Rmx = []
    Rmy = []
    Rmz = []
    rsumz = rsumy = rsum = 0

    ## Changes n for each case
    if Case == 1:
        n = 4
    if Case == 2:
        n = 6
    if Case == 3:
        n = 8


    Rfx = [F/n for F in Fx]         ## Reaction forces due to forces alone
    Rfy = [F/n for F in Fy]
    Rfz = [F/n for F in Fz]
    for i in range(len(rz)):
        r.append((rz[i]**2 + ry[i]**2)**0.5)            ## Calculates the radial distance
        alpha.append(pi/2-atan(ry[i]/rz[i]))            ## Calculates the angle between force and z axis
    if n == 4:
        for i in range(4):
            rsumz = rsumz + rz[0] ** 2
            rsumy = rsumy + ry[0] ** 2
            rsum = rsum + r[0] ** 2
    if n == 6:
        for i in range(4):
            rsumz = rsumz + rz[0] ** 2
            rsumy = rsumy + ry[0] ** 2
            rsum = rsum + r[0] ** 2
        for i in range(2):
            rsumz = rsumz + rz[1] ** 2
            rsumy = rsumy + ry[1] ** 2                          ## in-between calculation necesarry for Rm
            rsum = rsum + r[1] ** 2
    if n == 8:
        for i in range(4):
            rsumz = rsumz + rz[0] ** 2
            rsumy = rsumy + ry[0] ** 2
            rsum = rsum + r[0] ** 2
        for i in range(4):
            rsumz = rsumz + rz[1] ** 2
            rsumy = rsumy + ry[1] ** 2
            rsum = rsum + r[1] ** 2

    for i in range(len(rz)):
        for M in Mx:
            Rmz.append(M * r[i] / (n * rsum) * cos(alpha[i]))   ## Calculates the force due to moments
            Rmy.append(M * r[i] / (n * rsum) * sin(alpha[i]))
        for M1 in My:
            for M2 in Mz:
                Rmx.append(M1 * rz[i] / (n * rsumz) + M2 * ry[i] / (n * rsumy))

    Rx = FindAbsoluteMax(Rfx, Rmx)
    Ry = FindAbsoluteMax(Rfy, Rmy)
    Rz = FindAbsoluteMax(Rfz, Rmz)
    return [Rx, Ry, Rz]



