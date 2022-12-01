
## Environmental
Tmin = 271
Tmax = 307
Tassembly = 288.15
## Material properties
StressMax = 200                 ## MPa
EMod = 200 * 10 ** 3                      ## MPa
AlphaC = 2.6 * 10 ** -5
AlphaB = 1.25 * 10 ** -5
## Dimentions of the hole (distances, diameter, thickness)
D2 = 0.01
t2 = 0.01

## Other variables
Phi = 0.58

## intermediate calculations
Asm = D2*t2
DeltaT1 = Tmax - Tmin
DeltaT2 = abs(Tmax - Tassembly)
DeltaT3 = abs(Tmin - Tassembly)
DeltaT = max(DeltaT1, DeltaT2, DeltaT3)

## Force
FT = (AlphaC - AlphaB) * DeltaT * EMod * Asm * (1 - Phi) * 10 ** 6

