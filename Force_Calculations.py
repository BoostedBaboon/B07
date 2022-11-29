## Place where all forces are calculated on each fastener
import numpy as np
import math
from math import *

## Forces
Fx = [509.68, -509.68]
Fy = [1529.05, -509.68]
Fz = [509.68, -509.68]
Mx = [218.55, -159.94]
My = [29.306, -29.306]
Mz = [130.63, -130.63]

## Dimentions of the hole (distances, diameter, thickness)
rz = [0.5]
ry = [0.3]
D2 = 0.01
t2 = 0.001

## Material properties
StressMax = 200         ## MPa

## Creating empty lists and variables
r = []
alpha = []
Rmx = []
Rmy = []
Rmz = []
rsumx = rsumy = rsum = 0

## Multiple cases possible, 1 is a 4 fasterner config, 2 is a 6 fastener config, 3 is an 8 fastener config.
Case = 1

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
        rsumx = rsumx + rz[0] ** 2
        rsumy = rsumy + ry[0] ** 2
        rsum = rsum + r[0] ** 2
if n == 6:
    for i in range(4):
        rsumx = rsumx + rz[0] ** 2
        rsumy = rsumy + ry[0] ** 2
        rsum = rsum + r[0] ** 2
    for i in range(2):
        rsumx = rsumx + rz[1] ** 2
        rsumy = rsumy + ry[1] ** 2                          ## in-between calculation necesarry for Rm
        rsum = rsum + r[1] ** 2
if n == 8:
    for i in range(4):
        rsumx = rsumx + rz[0] ** 2
        rsumy = rsumy + ry[0] ** 2
        rsum = rsum + r[0] ** 2
    for i in range(4):
        rsumx = rsumx + rz[1] ** 2
        rsumy = rsumy + ry[1] ** 2
        rsum = rsum + r[1] ** 2

for i in range(len(rz)):
    for M in Mx:
        Rmz.append(M * r[i] / (n * rsum) * cos(alpha[i]))   ## Calculates the force due to moments
        Rmy.append(M * r[i] / (n * rsum) * sin(alpha[i]))
    for M1 in My:
        for M2 in Mz:
            Rmx.append(M1 * rz[i] / (n * rsumx) + M2 * ry[i] / (n * rsumy))

Rx = FindAbsoluteMax(Rfx, Rmx)
Ry = FindAbsoluteMax(Rfy, Rmy)
Rz = FindAbsoluteMax(Rfz, Rmz)

print("The maximum forces on a fastener is: Rx:", Rx, "N Ry:", Ry, "N Rz:", Rz, "N")

## Calculating the stresses:
RInPlane = (Rz ** 2 + Ry ** 2) ** 0.5
ROutPlane = Rx

Stress = RInPlane / (D2 * t2) / 10 ** 6     ## MPa
SafetyFactor = StressMax / Stress - 1



