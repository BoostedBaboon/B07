from Force_Calculations import CalculateForces
from Thermal_Forces import *
from Bearing_Check import CalculateBearing
from Hole_Dimentions import CalculateHoleDimensions, CalculateHoleDiameter
from Variables import *
from Variables import StrengthUltimate as StressMax
from Design import w as W
from Design import t as t1

## Calculation of other dimensions needed
L = AR * W

## Calculated Maximum diameters for each case
D2Calc1 = CalculateHoleDiameter(1, W, Metal)
D2Calc2 = CalculateHoleDiameter(2, W, Metal)
D2Calc3 = CalculateHoleDiameter(3, W, Metal)


## Chosen Diameters from the bolts (From Jasper)
print("The First Max Diameter is:", D2Calc1)
D2_1 = float(input("Enter Diameter 1:"))
DOuter1 = float(input("Enter Outer Diameter 1:"))
Compliance1 = float(input("Enter Compliance of Fastener 1:"))

print("The Second Max Diameter is:", D2Calc2)
D2_2 = float(input("Enter Diameter 2:"))
DOuter2 = float(input("Enter Outer Diameter 2:"))
Compliance2 = float(input("Enter Compliance of Fastener 2:"))

print("The Third Max Diameter is:", D2Calc3)
D2_3 = float(input("Enter Diameter 3:"))
DOuter3 = float(input("Enter Outer Diameter 3:"))
Compliance3 = float(input("Enter Compliance of Fastener 3:"))

## Calculates distances from CG to fastener hole
ry1 = CalculateHoleDimensions(1, D2_1, W, L, Metal)[0]
rz1 = CalculateHoleDimensions(1, D2_1, W, L, Metal)[1]

ry2 = CalculateHoleDimensions(2, D2_2, W, L, Metal)[0]
rz2 = CalculateHoleDimensions(2, D2_2, W, L, Metal)[1]

ry3 = CalculateHoleDimensions(3, D2_3, W, L, Metal)[0]
rz3 = CalculateHoleDimensions(3, D2_3, W, L, Metal)[1]

## Calculation of the Forces for each config
R1 = CalculateForces(1, rz1, ry1)
R2 = CalculateForces(2, rz2, ry2)
R3 = CalculateForces(3, rz3, ry3)


## Calculating PullthroughStress:

RInPlane1 = (R1[2] ** 2 + R1[1] ** 2) ** 0.5
RInPlane2 = (R2[2] ** 2 + R2[1] ** 2) ** 0.5
RInPlane3 = (R3[2] ** 2 + R3[1] ** 2) ** 0.5

ROutPlane1 = R1[0]
ROutPlane2 = R2[0]
ROutPlane3 = R3[0]

StressBearing1 = RInPlane1 / (D2_1 * t2) / 10 ** 6
StressBearing2 = RInPlane2 / (D2_2 * t2) / 10 ** 6
StressBearing3 = RInPlane3 / (D2_3 * t2) / 10 ** 6

SafetyFactorBearing1 = StressMax / StressBearing1 - 1
SafetyFactorBearing2 = StressMax / StressBearing2 - 1
SafetyFactorBearing3 = StressMax / StressBearing3 - 1

print("Pullthrough:", SafetyFactorBearing1, SafetyFactorBearing2, SafetyFactorBearing3)




## Calculating Bearing check

ShearStress1 = CalculateBearing(R1[0], D2_1, t2, t3, StressMax)
ShearStress2 = CalculateBearing(R2[0], D2_2, t2, t3, StressMax)
ShearStress3 = CalculateBearing(R3[0], D2_3, t2, t3, StressMax)

SafetyFactorShear1 = StressMax / ShearStress1 - 1
SafetyFactorShear2 = StressMax / ShearStress2 - 1
SafetyFactorShear3 = StressMax / ShearStress3 - 1

print("Bearing check", SafetyFactorShear1, SafetyFactorShear2, SafetyFactorShear3)

## Intermediate Calculations
ComplianceParts1 = 4 * t3 / (EModBackplate * pi * (DOuter1 ** 2 - D2_1 ** 2))
ComplianceParts2 = 4 * t3 / (EModBackplate * pi * (DOuter2 ** 2 - D2_2 ** 2))
ComplianceParts3 = 4 * t3 / (EModBackplate * pi * (DOuter3 ** 2 - D2_3 ** 2))

ForceRatio1 = ComplianceParts1 / (ComplianceParts1 + Compliance1)
ForceRatio2 = ComplianceParts2 / (ComplianceParts2 + Compliance2)
ForceRatio3 = ComplianceParts3 / (ComplianceParts3 + Compliance3)

## Calculating Thermal stresses:
FT1 = CalculateThermalForce(TExpansionFastener, TExpansionClamped, EMod, D2_1, t2, ForceRatio1)
FT2 = CalculateThermalForce(TExpansionFastener, TExpansionClamped, EMod, D2_2, t2, ForceRatio2)
FT3 = CalculateThermalForce(TExpansionFastener, TExpansionClamped, EMod, D2_3, t2, ForceRatio3)

RInPlane1 = RInPlane1 + FT1
RInPlane2 = RInPlane2 + FT2
RInPlane3 = RInPlane3 + FT3

StressThermal1 = RInPlane1 / (D2_1 * t2) / 10 ** 6     ## MPa
StressThermal2 = RInPlane2 / (D2_2 * t2) / 10 ** 6     ## MPa
StressThermal3 = RInPlane3 / (D2_3 * t2) / 10 ** 6     ## MPa

SafetyFactorThermal1 = StressMax / StressThermal1 - 1
SafetyFactorThermal2 = StressMax / StressThermal2 - 1
SafetyFactorThermal3 = StressMax / StressThermal3 - 1

print("Thermal Check", SafetyFactorThermal1, SafetyFactorThermal2, SafetyFactorThermal3)

print()
print("Current dimensions are:")
print("W =", W)
print("L =", L)
print("t1 =", t1)
print("t2 =", t2)
print("t3 =", t3)
print("D1 =", D1)
print("Config 1:")
print("D2 =", D2_1)
print("Config 2:")
print("D2 =", D2_2)
print("Config 3:")
print("D2 =", D2_3)
print()
print("Using", MaterialName)
