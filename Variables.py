from math import *

## Forces (Not changeable)
Fx = [509.68, -509.68]
Fy = [1529.05, -509.68]
Fz = [509.68, -509.68]
Mx = [218.55, -159.94]
My = [29.306, -29.306]
Mz = [130.63, -130.63]

## Dimensions of the lug (some changeable)
AR = 10
t2 = 0.001
t3 = 0.001
D1 = 0.01



## Material properties (Changeable)
MaterialName = ""               ## Enter your material name here !!!!
Metal = True
StrengthYield = 140             ## MPa
StrengthUltimate = 210          ## MPa
EMod = 200 * 10 ** 3                    ## MPa
EModBackplate = 200 * 10 ** 3           ## MPa
TExpansionFastener = 0.0065             ## ()
TExpansionClamped = 0.0070              ## ()

## Environmental conditions
Tmin = 271
Tmax = 307
Tassembly = 288.15