import math
import matplotlib
from Variables import Fy, Mx, My

Fy = 1
Nf = 1
Mx = [1, 2, 3, 4]
My = [1, 2, 3, 4]
Ai = [1, 2, 3, 4]
ri = [1, 2, 3, 4]
FpMx = []
FpMy = []
FLoad = []
FpMxiBot = 0
FpMyiBot = 0

# Calc out of plane load for F
Fpi = Fy / Nf


# Function to order list
def TakeSecond(elem):
    return elem[1]


# Calc out of plane load for Mx
for i in range(len(Ai)):

    for m in range(len(Ai)):
        FpMxiAdd = Ai[m] * ((ri[m]) ** 2)
        FpMxiBot = FpMxiBot + FpMxiAdd

    FpMxiTop = (Mx[i] * Ai[i] * ri[i])

    FpMxi = FpMxiTop / FpMxiBot

    FpMx.append(FpMxi)

# Calc out of plane load for My
for i in range(len(Ai)):

    for m in range(len(Ai)):
        FpMyiAdd = Ai[m] * ((ri[m]) ** 2)
        FpMyiBot = FpMyiBot + FpMyiAdd

    FpMyiTop = (My[i] * Ai[i] * ri[i])

    FpMyi = FpMyiTop / FpMyiBot

    FpMy.append(FpMyi)

# Add all out of plane loads together and add to a list
for b in range(len(FpMy)):
    FLoadi = FpMx[b] + FpMy[b] + Fpi

    FLugi = [b, FLoadi]

    FLoad.append(FLugi)

# Sort and print list
FLoad.sort(reverse=True, key=TakeSecond)
# print(FLoad)

# -----------------------------------------

Dfi = 1  # ADD
t2 = 1  # ADD
t3 = 1  # ADD
N = 1  # ADD
def CalculateBearing(N, D2, t2, t3, Y):
    # Calc Shear stress
    ShearStresst2 = N / (math.pi * D2 * t2) / 10 ** 6

    ShearStresst3 = N / (math.pi * D2 * t3) / 10 ** 6

    # print("Shear Stress t2:", ShearStresst2)
    # print("Shear Stress t3:", ShearStresst3)

    # Print whether it passes check or not
    if Y < ShearStresst2:
        print("Not Sufficient for t2")
    elif Y < ShearStresst3:
        print("Not Sufficient for t3")
    else:
        print("Sufficient")
    return max(ShearStresst2, ShearStresst3)


