from Variables import Tmin, Tmax, Tassembly

## intermediate calculations
DeltaT1 = Tmax - Tmin
DeltaT2 = abs(Tmax - Tassembly)
DeltaT3 = abs(Tmin - Tassembly)
DeltaT = max(DeltaT1, DeltaT2, DeltaT3)


## Force
def CalculateThermalForce(TExpansionClamped, TExpansionFastener, EModulus, D2, t2, Phi):
    F = (TExpansionClamped - TExpansionFastener) * DeltaT * EModulus * D2 * t2 * (1 - Phi) * 10 ** 6
    return F

